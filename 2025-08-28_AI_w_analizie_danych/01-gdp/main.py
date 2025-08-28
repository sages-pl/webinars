import pandas as pd
import matplotlib.pyplot as plt


DATA_GDP = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
DATA_POPULATION = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
USD = 1
INCH = 1

COUNTRIES = {
    'Hong Kong (China)': 'Hong Kong',
    'Puerto Rico (US)': 'Puerto Rico',
    'Democratic Republic of the Congo': 'DR Congo',
    'Macau (China)': 'Macau',
    'Republic of the Congo': 'Congo',
    'New Caledonia (France)': 'New Caledonia',
    'Bermuda (UK)': 'Bermuda',
    'Isle of Man (UK)': 'Isle of Man',
    'Cayman Islands (UK)': 'Cayman Islands',
    'Guam (US)': 'Guam',
    'French Polynesia (France)': 'French Polynesia',
    'U.S. Virgin Islands (US)': 'U.S. Virgin Islands',
    'Aruba (Netherlands)': 'Aruba',
    'Faroe Islands (Denmark)': 'Faroe Islands',
    'Greenland (Denmark)': 'Greenland',
    'Curaçao (Netherlands)': 'Curaçao',
    'Turks and Caicos Islands (UK)': 'Turks and Caicos Islands',
    'Sint Maarten (Netherlands)': 'Sint Maarten',
    'British Virgin Islands (UK)': 'British Virgin Islands',
    'Northern Mariana Islands (US)': 'Northern Mariana Islands',
    'American Samoa (US)': 'American Samoa',
    'Saint Martin (France)': 'Saint Martin',
    'Anguilla (UK)': 'Anguilla',
    'Cook Islands (New Zealand)': 'Cook Islands',
    'Montserrat (UK)': 'Montserrat'
}

# %%

gdp = (
    pd
    .read_html(DATA_GDP, storage_options={'User-Agent': USER_AGENT})[2]
    .loc[:, [
        ('Country/Territory', 'Country/Territory'),
        ('United Nations[8]', 'Estimate')
    ]]
    .droplevel(level=0, axis='columns')
    .rename(columns={'Country/Territory': 'country', 'Estimate': 'gdp'})
    .replace({'gdp': {'—': pd.NA}}, regex=True)
    .dropna(how='any', subset=['gdp'], axis='rows')
    .astype({'gdp': 'Int64'})
    .assign(gdp=lambda df: df['gdp'].mul(1_000_000*USD))
    .convert_dtypes()
)

# %%

population = (
    pd
    .read_html(DATA_POPULATION, storage_options={'User-Agent': USER_AGENT})[0]
    .loc[:, ['Location', 'Population']]
    .rename(columns={'Location': 'country', 'Population': 'population'})
    .replace({'country': COUNTRIES})
    .astype({'population': 'Int64'})
    .convert_dtypes()
)

# %%

result = (
    population
    .merge(gdp, on='country', how='inner')
    .assign(
        percapita=lambda df: df['gdp'] / df['population']
    )
    .round({'percapita': 2})
    .convert_dtypes()
    .sort_values(by='percapita', ascending=False)
)

top10 = (
    result
    .head(10)
).plot(
    x='country',
    y='percapita',
    kind='bar',
    figsize=(12*INCH, 8*INCH),
    title='Top 10 krajów według PKB per capita',
    xlabel='Kraje',
    ylabel='PKB per capita (USD)',
    rot=45
)

plt.tight_layout()
plt.show()
