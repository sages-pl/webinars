import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.width', 300)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)


LUDNOSC = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_liczby_ludno%C5%9Bci'
PKB = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_PKB_(parytet_si%C5%82y_nabywczej)'

#%%
USD = 1

pkb: pd.DataFrame = (
    pd
    .read_html(PKB)[0]
    .convert_dtypes()
    .loc[:, ['Kraj', '2019']]
    .rename(columns={'2019': 'PKB'})
    .replace('b.d', pd.NA)
    .replace('\[2\]', '', regex=True)
    .set_index('Kraj')
    .replace(' ', '', regex=True)
    .dropna()
    .astype('int')
    .mul(1_000_000*USD))

pkb.info(memory_usage='deep')


#%%
ludnosc = (
    pd
    .read_html(LUDNOSC)[0]
    .droplevel(level=0, axis='columns')
    .rename(columns={
        '2022': 'Ludność',
        'Państwo, obszar lub terytorium zależne': 'Kraj'})
    .loc[:, ['Kraj', 'Ludność']]
    .replace({
        'Chińska Republika Ludowa': 'Chiny',
        'Korea Północna': pd.NA,
        'Republika Chińska': 'Tajwan',
        'Kuba': pd.NA,
        'Zachodni Brzeg': pd.NA,
        'Strefa Gazy': pd.NA,
        'Syria': pd.NA})
    .dropna()
    .set_index('Kraj')
    .replace('\xa0', '', regex=True)
    .replace('\[3\]', '', regex=True)
    .replace('–', pd.NA, regex=True)
    .replace(' ', '', regex=True)
    .dropna()
    .astype('int'))

ludnosc.info(memory_usage='deep')

#%%
result = (
    pkb.merge(ludnosc, left_index=True, right_index=True)
    .sort_index(ascending=True)
    .eval('PerCapita = PKB / Ludność'))

#%%
plot = (
    result
    .loc[:, ['PerCapita']]
    .round(1)
    .sort_values('PerCapita', ascending=False)
    .head(n=30)
    .plot(kind='bar', legend=True, grid=True, figsize=(16,10)))

plt.show()
