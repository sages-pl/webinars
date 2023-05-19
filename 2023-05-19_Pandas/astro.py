# https://github.com/sages-pl/webinars
# https://www.pola.rs/
# https://www.dask.org/

import pandas as pd


pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)

URL = 'https://en.wikipedia.org/wiki/European_Astronaut_Corps'

tables = pd.read_html(URL)
current = tables[0]
former = tables[2]

c = current['Time in space'].apply(pd.to_timedelta).sum()
f = former['Time in space'].apply(pd.to_timedelta).sum()

total = round((c+f).days / 365.25, ndigits=1)
