import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


pd.set_option('display.width', 300)
pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 100)
pd.set_option('display.min_rows', 100)
pd.set_option('display.max_seq_items', 100)


URL = 'https://python3.info/_static/sensors-optima.xlsx'

LUX = 1
LIGHT_NOISE_THRESHOLD = 20 * LUX

# %%

def were_active(df):
    return df['value'] > LIGHT_NOISE_THRESHOLD


def mission_day(df):
    mission_start = df.index.min()
    mission_end = df.index.max()
    mission_days = pd.date_range(mission_start, mission_end, freq='D', normalize=True).date
    to_replace = {date:i for i,date in enumerate(mission_days)}
    return df['date'].replace(to_replace)

# %%
df = (
    pd.read_excel(
        io=URL,
        sheet_name='Luminance',
        header=1,
        parse_dates=['datetime'],
        usecols=['datetime', 'device', 'location', 'value', 'type'],
        index_col='datetime')
    .assign(
        date = lambda df: df.index.date,
        time = lambda df: df.index.round(freq='s').time,
        day = lambda df: mission_day(df),
        hour = lambda df: df.index.hour,
        activity = lambda df: were_active(df).astype('int'))
    .convert_dtypes()
)

df.info(memory_usage='deep')

#%%

data = (
    df
    .loc[:, 'value']
    .resample('H')
    .mean()
    .round()
    .astype('int16'))

ax: plt.Axes = data.plot(
    kind='line',
    title='Zmiany w oświetleniu w trakcie misji',
    xlabel='Mission Day',
    ylabel='Illuminance [lux]',
    figsize=(8,8))

ax.set_xticklabels(range(0,7), minor=True)
ax.set_xmargin(0)
plt.show()

#%%

data = (
    df
    .loc[:, ['day', 'hour', 'value']]
    .groupby(['day', 'hour'])
    .mean()
    .round()
    .astype('int16')
    .reset_index()
    .pivot(index='day', columns='hour', values='value'))

rows = [f'Day {day}' for day in range(data.index.size)]
columns = [f'{hour:02}:00' for hour in data.columns]
values = data.values

fig, ax = plt.subplots(figsize=(15,5))
im = ax.imshow(values)

ax.set_yticks(np.arange(len(rows)), labels=rows)
ax.set_xticks(np.arange(len(columns)), labels=columns)
ax.set_title('Actinogram')
ax.set_xlabel('Time of a day [UTC]')
ax.set_ylabel('Mission day')

plt.setp(ax.get_xticklabels(), rotation=90, ha='right', rotation_mode='anchor')

fig.colorbar(im, ax=ax, shrink=0.85, label='Luminescence [lux]')
fig.tight_layout()

plt.show()
