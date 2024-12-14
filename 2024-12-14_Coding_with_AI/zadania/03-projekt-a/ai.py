# GDP = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
# POPULATION = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'

GDP = 'data/gdp.html'
POPULATION = 'data/population.html'

import pandas as pd

# Read GDP data
gdp = pd.read_html(GDP)[0]
gdp.columns = gdp.columns.droplevel()
gdp = gdp[['Country/Territory', 'GDP(US$million)']]
gdp.columns = ['Country', 'GDP']

# Read population data
population = pd.read_html(POPULATION)[0]
population.columns = population.columns.droplevel()
population = population[['Country (or dependent territory)', 'Population']]
population.columns = ['Country', 'Population']

# Merge data
data = pd.merge(gdp, population, on='Country')

# Save data
data.to_csv('data.csv', index=False)
print(data)

