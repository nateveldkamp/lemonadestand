#%% imports
import math
from random import random
def weather():
    r = random()
    if r < 0.6: weather = 'Sunny'
    elif r < 0.8: weather = 'Cloudy'
    else: weather = 'Hot'  
    return weather 
def results(weather, glasses, signs, price):
    if weather == 'Cloudy': weather_factor=.5
    elif weather == 'Hot': weather_factor=2.0
    else: weather_factor=1.0
    base_demand = 20-price
    marketing_uplift = 1+(1-math.exp(-signs))
    demand = weather_factor * base_demand * marketing_uplift
    sales = min(demand, glasses)
    revenues = sales * price/100
    expenses = glasses * .03
    profit = revenues - expenses
    return sales,revenues,expenses,profit
weather = weather()
print(weather)
results = results(weather, glasses=50, signs=1, price=12)
print(results)