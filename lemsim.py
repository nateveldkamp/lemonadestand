#%% imports
import sys
sys.path.append('../functions')
from functions import get_ls_results
import json
import pandas as pd
import math
from random import random
#%% 
days = 10000
price = [i for i in range(6, 20)]          # range(0, 101)
signs = [i for i in range(0, 10)]           # range(0, 21)
glasses = [i for i in range(0, 150)]       # range(10, 201)
w = {'Assets': 10.00}

#%%
day = 1
l = []
while day <= days:
    assets = w['Assets']
    get_price = math.floor(len(price)*random())
    get_signs = math.floor(len(signs)*random())
    get_glasses = math.floor(len(glasses)*random())
    w = get_ls_results(get_glasses, get_signs, get_price, day=day, assets=assets)
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
    , 'ChanceOfRain'
    , 'BaseDemand'
    , 'SignBenefit'
    , 'DemandMultiplier'
    , 'AdjUnits'
    , 'CostPerGlass'
    , 'CostPerSign'
    , 'Income'
    , 'Expenses'
]]
# df
#%% write results to files
df.to_csv('data/lem_stand_results.csv', index=False)
df.to_excel('data/lem_stand_results.xlsx', sheet_name='Sheet1', index=False)
df.to_json('data/test.json', orient='records')