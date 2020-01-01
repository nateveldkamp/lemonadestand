#%% imports
from lemonadestand import get_weather, get_ls_results
import pandas as pd
import random
# import json
# import math
#%%
def get_inputs(weather):
    if weather == 'Hot':
        signs = random.choice(list(range(0,8)))
        price = random.choice(list(range(6,15)))
        glasses = random.choice(list(range(60,160))) if price <= 10 or signs >=2 else random.choice(list(range(40,130)))
        return glasses, signs, price
    elif weather == 'Sunny':
        glasses = random.choice(list(range(40,60)))
        signs = random.choice(list(range(0,6)))
        price = random.choice(list(range(6,12)))
        return glasses, signs, price
    elif weather == 'Cloudy':
        signs = random.choice(list(range(0,4)))
        price = random.choice(list(range(6,10)))
        glasses = random.choice(list(range(20,80))) if price <= 10 and signs >=2 else random.choice(list(range(5,40)))
        return glasses, signs, price
# get_inputs(weather='Sunny')

#%%
days = 10000
w = {'Assets': 10.00}
day = 1
l = []
while day <= days:
    assets = w['Assets']
    weather = get_weather(day)
    glasses, signs, price = get_inputs(weather)
    w = get_ls_results(glasses, signs, price
            ,weather=weather, day=day, assets=assets)
    l.append(w)
    day += 1
df = pd.DataFrame(l)
# show results
df = df[[
      'Day'
    , 'Weather'
    , 'PricePerGlass'
    , 'SignsMade'
    , 'GlassesMade'
    , 'GlassesSold'
    , 'Profit'
    , 'Assets'
    , 'Storm'
    , 'StreetCrewWorking'
    , 'StreetCrewThirsty'
    , 'WeatherFactor'
    , 'MarketingFactor'
    , 'DemandMultiplier'
    , 'AdjDemand'
    , 'ChanceOfRain'
    , 'BaseDemand'
    , 'CostPerGlass'
    , 'CostPerSign'
    , 'Income'
    , 'Expenses'
]]

#%% view header
df.head(20)

#%% write results to files
df.to_csv('data/ls_results.csv', index=False)
# df.to_excel('data/ls_results.xlsx', sheet_name='Sheet1', index=False)
# df.to_json('data/ls_results.json', orient='records')

# %%
