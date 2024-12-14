import pandas as pd
from matplotlib import pyplot as plt

# %%

# GDP = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
# POPULATION = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

GDP = 'data/gdp.html'
POPULATION = 'data/population.html'
USD = 1

COUNTRIES = {
    'Democratic Republic of the Congo': 'DR Congo',
    'Hong Kong (China)': 'Hong Kong',
    'Republic of the Congo': 'DR Congo',
    'Puerto Rico (US)': 'Puerto Rico',
    'Macau (China)': 'Macau',
    'Western Sahara': pd.NA,
    'Northern Cyprus': pd.NA,
    'Transnistria': pd.NA,
    'French Polynesia (France)': 'French Polynesia',
    'New Caledonia (France)': '',
    'Abkhazia': '',
    'Curaçao (Netherlands)': '',
    'Guam (US)': '',
    'Aruba (Netherlands)': '',
    'Jersey (UK)': '',
    'U.S. Virgin Islands (US)': '',
    'Cayman Islands (UK)': '',
    'Isle of Man (UK)': '',
    'Guernsey (UK)': '',
    'Bermuda (UK)': '',
    'Greenland (Denmark)': '',
    'South Ossetia': '',
    'Faroe Islands (Denmark)': '',
    'American Samoa (US)': '',
    'Turks and Caicos Islands (UK)': '',
    'Northern Mariana Islands (US)': '',
    'Sint Maarten (Netherlands)': 'Sint Maarten',
    'Gibraltar (UK)': '',
    'Saint Martin (France)': '',
    'British Virgin Islands (UK)': '',
    'Anguilla (UK)': '',
    'Cook Islands': '',
    'Wallis and Futuna (France)': '',
    'Saint Barthélemy (France)': '',
    'Saint Pierre and Miquelon (France)': '',
    'Saint Helena, Ascension and Tristan da Cunha (UK)': '',
    'Montserrat (UK)': '',
    'Falkland Islands (UK)': '',
    'Norfolk Island (Australia)': '',
    'Christmas Island (Australia)': '',
    'Niue (New Zealand)': '',
    'Tokelau (New Zealand)': '',
    'Vatican City': '',
    'Cocos (Keeling) Islands (Australia)': '',
    'Pitcairn Islands (UK)': '',
}

# %%

gdp = (
    pd
    .read_html(GDP)[2]
    .loc[:, [('Country/Territory', 'Country/Territory'),
             ('United Nations[15]', 'Estimate')]]
    .droplevel(level=0, axis='columns')
    .rename(columns={'Country/Territory': 'country', 'Estimate': 'gdp'})
    .replace({'gdp': {'—': pd.NA}, 'countries':COUNTRIES})
    .dropna(how='any', axis='rows')
    .astype({'gdp': 'Int64'})
    .convert_dtypes()
    .set_index('country')
    .multiply(1_000_000 * USD)
)
gdp

# %%

population = (
    pd
    .read_html(POPULATION)[0]
    .loc[:, ['Location', 'Population']]
    .rename(columns={'Location': 'country', 'Population': 'population'})
    .convert_dtypes()
    .set_index('country')
)
population

# %%

data = (
    pd
    .merge(gdp, population, on='country')
    .assign(percapita=lambda df: df['gdp'] / df['population'])
    .round(2)
)
data


#%%


top_10 = (
    data
    .nlargest(10, 'percapita')
).plot(
    kind='bar',
    y='percapita',
    figsize=(10, 6),
    color='blue',
    legend=False,
    xlabel='Country',
    ylabel='GDP per capita',
    title='Top 10 countries by GDP per capita',
)

plt.tight_layout()
plt.savefig('top10.png')
