# python3 -m pip install pandas matplotlib

import pandas as pd
from matplotlib import pyplot as plt

#%%

pd.set_option('display.width', 300)
pd.set_option('display.max_columns', 25)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)
pd.set_option('display.float_format', '{:.2f}'.format)

#%%

PKB = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_PKB_nominalnego'
LUDNOSC = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_liczby_ludno%C5%9Bci'
USD = 1

KRAJE = {
    'Chińska Republika Ludowa': 'Chiny',
    'Francja[a]': 'Francja',
    'Korea Północna': pd.NA,
    'Republika Chińska': 'Tajwan',
    'Holandia[b]': 'Holandia',
    'Kuba': pd.NA,
    'Zachodni Brzeg': 'Zachodni Brzeg i Strefa Gazy',
    'Strefa Gazy': pd.NA,
    'Sahara Zachodnia': pd.NA,
    'Polinezja Francuska': pd.NA,
    'Nowa Kaledonia': pd.NA,
    'Guam': pd.NA,
    'Curaçao': pd.NA,
    'Wyspy Dziewicze': pd.NA,
    'Afganistan': pd.NA,
    'Liban': pd.NA,
    'Syria': pd.NA,
}


#%%

ludnosc = (
    pd
    .read_html(LUDNOSC)[0]
    .droplevel(0, axis='columns')
    .rename(columns={'Państwo, obszar lub terytorium zależne':'kraj', '2022':'ludnosc'})
    .replace({'kraj': KRAJE})
    .loc[:, ['kraj', 'ludnosc']]
    .replace({'ludnosc': {r'\[\d\]':'', '\xa0':'', r'\s':'', '–':0}}, regex=True)
    .astype({'kraj':str, 'ludnosc':int})
    .convert_dtypes()
    .set_index('kraj', drop=True)
    .sort_values('ludnosc', ascending=False)
)

# ludnosc.info(memory_usage='deep')
# <class 'pandas.core.frame.DataFrame'>
# Index: 243 entries, Świat to Georgia Południowa i Sandwich Południowy
# Data columns (total 1 columns):
#  #   Column   Non-Null Count  Dtype
# ---  ------   --------------  -----
#  0   ludnosc  243 non-null    Int64
# dtypes: Int64(1)
# memory usage: 17.1 KB

#%%

pkb = (
    pd
    .read_html(PKB)[2]
    .rename(columns={'Państwo':'kraj', '2022 r.':'pkb'})
    .loc[:, ['kraj', 'pkb']]
    .replace({'pkb': {r'\s':'', 'b.d.':0}}, regex=True)
    .astype({'kraj':str, 'pkb':int})
    .convert_dtypes()
    .set_index('kraj', drop=True)
    .sort_values('pkb', ascending=False)
    .mul({'pkb': 1_000_000*USD})
)

# pkb.info(memory_usage='deep')
# <class 'pandas.core.frame.DataFrame'>
# Index: 199 entries, Świat to Syria
# Data columns (total 1 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   pkb     199 non-null    Int64
# dtypes: Int64(1)
# memory usage: 13.7 KB

#%%


pkb.query('kraj not in @ludnosc.index')
#                        pkb
# kraj
# Strefa euro  14128210000000

ludnosc.query('kraj not in @pkb.index')
#                                                      ludnosc
# kraj
# <NA>                                                25955138
# <NA>                                                11008112
# <NA>                                                 1997328
# <NA>                                                  576000
# <NA>                                                  299356
# <NA>                                                  297160
# <NA>                                                  169086
# <NA>                                                  152379
# <NA>                                                  105413
# Jersey                                                102146
# Wyspa Man                                              91382
# Bermudy                                                72337
# Guernsey                                               67491
# Kajmany                                                64309
# Turks i Caicos                                         58286
# Grenlandia                                             57792
# Wyspy Owcze                                            52269
# Mariany Północne                                       51475
# Samoa Amerykańskie                                     45443
# Sint Maarten                                           45126
# Liechtenstein                                          39711
# Brytyjskie Wyspy Dziewicze                             38632
# Saint-Martin[c]                                        32792
# Monako                                                 31400
# Gibraltar                                              29573
# Anguilla                                               18741
# Wallis i Futuna                                        15891
# Wyspy Cooka                                             8128
# Wyspa Świętej Heleny, Wyspa Wniebowstąpienia i ...      7925
# Saint-Barthélemy[c]                                     7103
# Montserrat                                              5414
# Saint-Pierre i Miquelon                                 5257
# Falklandy                                               3198
# Svalbard                                                2926
# Niue                                                    2000
# Tokelau                                                 1647
# Watykan                                                 1000
# Pitcairn                                                  50
# Norfolk                                                    0
# Wyspa Bożego Narodzenia                                    0
# Wyspy Kokosowe                                             0
# Majotta                                                    0
# Dhekelia                                                   0
# Akrotiri                                                   0
# Georgia Południowa i Sandwich Południowy                   0

#%%

data = (
    pkb
    .merge(ludnosc, left_index=True, right_index=True, how='inner')
    .assign(percapita=lambda df: df['pkb'] / df['ludnosc'])
    .round({'percapita': 2})
    .astype({'percapita': 'Float64'})
    .convert_dtypes()
    .sort_values(by='percapita', ascending=False)
)

#%%

top = (
    data
    .head(n=70)
    .loc[:, 'percapita']
    .plot(
        kind='bar',
        title='PKB per capita',
        xlabel='Kraj',
        ylabel='PKB per capita [USD]',
        figsize=(15, 10),
        grid=False,
        legend=True,
    )
)

plt.tight_layout()
plt.show()

#%%

bottom30 = (
    data
    .tail(n=30)
    .loc[:, 'percapita']
    .plot(
        kind='bar',
        title='PKB per capita - 30 najbiedniejszych krajów',
        xlabel='Kraj',
        ylabel='PKB per capita [USD]',
        figsize=(15, 10),
        grid=False,
        legend=True,
        color='red',
        edgecolor='black'
    )
)

plt.tight_layout()
plt.show()
