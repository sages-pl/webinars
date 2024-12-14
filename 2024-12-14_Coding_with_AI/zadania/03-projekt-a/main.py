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

def get_gdp(file):
    """
    >>> result = get_gdp(GDP)

    >>> result.head(5)  # doctest: +NORMALIZE_WHITESPACE
                               gdp
    country
    World          100834796000000
    United States   25744100000000
    China           17963170000000
    Germany          4076923000000
    Japan            4232173000000

    >>> result.loc['World']
    gdp    100834796000000
    Name: World, dtype: Int64

    >>> result.loc['Poland']
    gdp    688125000000
    Name: Poland, dtype: Int64

    >>> result.info(memory_usage='deep')  # doctest: +NORMALIZE_WHITESPACE
    <class 'pandas.core.frame.DataFrame'>
    Index: 209 entries, World to Tuvalu
    Data columns (total 1 columns):
     #   Column  Non-Null Count  Dtype
    ---  ------  --------------  -----
     0   gdp     209 non-null    Int64
    dtypes: Int64(1)
    memory usage: 21.7 KB
    """
    return (
        pd
        .read_html(file)[2]
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

# %%

def get_population(file):
    """
    >>> result = get_population(POPULATION)

    >>> result.head(5)  # doctest: +NORMALIZE_WHITESPACE
                   population
    country
    World          8119000000
    China          1409670000
    India          1404910000
    United States   335893238
    Indonesia       282477584

    >>> result.loc['World']
    population    8119000000
    Name: World, dtype: Int64

    >>> result.loc['Poland']
    population    37532000
    Name: Poland, dtype: Int64

    >>> result.info(memory_usage='deep')  # doctest: +NORMALIZE_WHITESPACE
    <class 'pandas.core.frame.DataFrame'>
    Index: 240 entries, World to Pitcairn Islands (UK)
    Data columns (total 1 columns):
     #   Column      Non-Null Count  Dtype
    ---  ------      --------------  -----
     0   population  240 non-null    Int64
    dtypes: Int64(1)
    memory usage: 24.2 KB
    """
    return (
        pd
        .read_html(file)[0]
        .loc[:, ['Location', 'Population']]
        .rename(columns={'Location': 'country', 'Population': 'population'})
        .convert_dtypes()
        .set_index('country')
    )

# %%

def get_data(gdp, population):
    """
    >>> gdp = get_gdp(GDP)
    >>> population = get_population(POPULATION)
    >>> result = get_data(gdp, population)

    >>> result.head(5)  # doctest: +NORMALIZE_WHITESPACE
                                   gdp  population  percapita
    country
    World          100834796000000  8119000000   12419.61
    United States   25744100000000   335893238    76643.7
    China           17963170000000  1409670000   12742.82
    Germany          4076923000000    84708010   48129.13
    Japan            4232173000000   123790000   34188.33

    >>> result.loc['World']
    gdp           100834796000000.0
    population         8119000000.0
    percapita              12419.61
    Name: World, dtype: Float64

    >>> result.loc['Poland']
    gdp           688125000000.0
    population        37532000.0
    percapita           18334.35
    Name: Poland, dtype: Float64

    >>> result.info(memory_usage='deep')  # doctest: +NORMALIZE_WHITESPACE
    <class 'pandas.core.frame.DataFrame'>
    Index: 194 entries, World to Tuvalu
    Data columns (total 3 columns):
     #   Column      Non-Null Count  Dtype
    ---  ------      --------------  -----
     0   gdp         194 non-null    Int64
     1   population  194 non-null    Int64
     2   percapita   194 non-null    Float64
    dtypes: Float64(1), Int64(2)
    memory usage: 20.1 KB
    """
    return (
        pd
        .merge(gdp, population, on='country')
        .assign(percapita=lambda df: df['gdp'] / df['population'])
        .round({'percapita': 2})
        .astype({'gdp': 'Int64', 'population': 'Int64', 'percapita': 'Float64'})
    )


#%%

gdp = get_gdp(GDP)
population = get_population(POPULATION)
data = get_data(gdp, population)

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
