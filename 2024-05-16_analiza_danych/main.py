"""
Python w analizie danych

Język Python i biblioteki Pandas oraz Matplotlib stały się głównymi
narzędziami wykorzystywanymi w data science. Nauczenie się korzystania
z podstawowych funkcjonalności tych modułów nie jest trudne i każdy
w ciągu kilku dni może zacząć z nimi pracować. Jednakże opanowanie
trudniejszych aspektów tj. indeksy multi-kolumnowe, przecięcia poprzeczne,
grupowania, zaawansowane agregacje, różnice przyrostowe, tabele przestawne,
scalania i łączenia, przesunięcia-wędrujące itp., stanowią wyzwanie
do samodzielnej nauki. I chociaż wszystkie materiały są dostępne w internecie,
to bardzo dużo czasu można zaoszczędzić, gdy opowie o nich ktoś, kto starannie
wyselekcjonował program, dobrał przykłady i ćwiczenia tak, aby stopniowo
wprowadzały w zaawansowane tematy i nie przytłaczały natłokiem informacji.

Zapraszam na nasz najnowszy webinar dotyczący Python, Pandas i Matplotlib.
Podczas wykładu słuchacz zobaczy jakie umiejętności nabędzie podczas kursu
"Analiza i wizualizacja danych w Python". Wspólnie przejdziemy studium
przypadku analizy danych i wizualizacji. Gwarantuję, że to będzie bardzo
owocnie poświęcone 90 minut.

1. Przejdziemy studium przypadku analizy danych i wizualizacji
2. Oczyścimy dane i przygotujemy je do wizualizacji
3. Poznamy jak wygenerować wykresy z danych z Pandas

Trener:
https://www.sages.pl/o-nas/zespol/matt-harasymczuk

Materiały:
https://python3.info/

Kurs:
https://python.kodolamacz.pl/
https://platforma.sages.pl/product/python-w-analizie-danych/
https://platforma.sages.pl/python-w-analizie-danych/

Kod źródłowy z dzisiejszego webinaru:
https://github.com/sages-pl/webinars/tree/main/2024-05-16_analiza_danych

Dane:
https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_liczby_ludno%C5%9Bci
https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_PKB_(parytet_si%C5%82y_nabywczej)
"""

#%%

import pandas as pd
import matplotlib.pyplot as plt


LUDNOSC = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_liczby_ludno%C5%9Bci'
PKB = 'https://pl.wikipedia.org/wiki/Lista_pa%C5%84stw_%C5%9Bwiata_wed%C5%82ug_PKB_(parytet_si%C5%82y_nabywczej)'
USD = 1

#%%

ludnosc = (
    pd
    .read_html(LUDNOSC)[0]
    .droplevel(level=0, axis='columns')
    .rename(columns={
        'Państwo, obszar lub terytorium zależne': 'kraj',
        '2022': 'ludnosc'})
    .loc[:, ['kraj', 'ludnosc']]
    .replace({
        'kraj': {r'\[a\]': ''},
        'ludnosc': {r'\[3\]': '', '\xa0': '', ' ': '', '–': pd.NA},
    }, regex=True)
    .replace({'kraj': {
        'Chińska Republika Ludowa': 'Chiny',
        'Zachodni Brzeg i Strefa Gazy': 'Zachodni Brzeg',
        'Tajwan': pd.NA,
    }})
    .dropna(axis='rows', how='any')
    .astype({'ludnosc': 'Int64', 'kraj': 'string'})
    .convert_dtypes()
    .set_index('kraj')
    .sort_index(ascending=True)
)

#%%

pkb = (
    pd
    .read_html(PKB)[0]
    .rename(columns={
        '2019': 'pkb',
        'Kraj': 'kraj'})
    .loc[:, ['kraj', 'pkb']]
    .replace({
        'kraj': {r'\[2\]': ''},
        'pkb': {r'\s': '', 'b.d': pd.NA}
    }, regex=True)
    .astype({'pkb': 'Int64', 'kraj': 'string'})
    .convert_dtypes()
    .dropna(axis='rows', how='any')
    .set_index('kraj')
    .sort_index(ascending=True)
    .mul(1_000_000*USD)
)

#%%

result = (
    pkb
    .merge(ludnosc, left_index=True, right_index=True)
    .assign(percapita=lambda df: df['pkb'] / df['ludnosc'])
    .sort_values(by='percapita', ascending=False)
    .head(10)
    .loc[:, ['percapita']]
    .round()
    .astype('Int64')
    .convert_dtypes()
)

#%%

result.plot(
    kind='bar',
    title='PKB per capita',
    xlabel='Kraj',
    ylabel='PKB per capita [USD]',
    figsize=(15, 10),
    grid=False,
)

plt.tight_layout()
plt.show()

#%%

# Wykrywanie, które kraje są w obu zbiorach
# p = pkb.index
# l = ludnosc.index
# query = p.isin(l)
# p[query]
