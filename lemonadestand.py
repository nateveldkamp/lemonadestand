#%% imports
import math
from random import random

#%% weather
def get_weather(day=1):
    r = random()
    if r < 0.6:     # 60% chance Sunny
        weather = 'Sunny'
    elif r < 0.8:   # 20% chance Cloudy
        weather = 'Cloudy'
    else:           # 20% chance HOT
        if day < 3:
            weather = 'Sunny'
        else:
            weather = 'Hot'
    return weather
# get_weather(15)

#%% rain
def get_chance_of_rain(weather):
    if weather == 'Cloudy':
        chance_of_rain = 30 + math.floor(random() * 5) * 10
    else:
        chance_of_rain = 0
    return chance_of_rain
# get_chance_of_rain('Cloudy')

#%% storm
def get_storm(weather):
    storm = False
    if weather == 'Cloudy':
        if random() < 0.25:
            storm = True
    return storm
# get_storm('Sunny')

#%% street crew
def get_street_crew(weather):
    street_crew_working = False
    street_crew_thirsty = False
    if weather == 'Sunny':
        if random() <= 0.25:
            street_crew_working = True
            if random() < 0.5:
                street_crew_thirsty = True
    return street_crew_working, street_crew_thirsty
# get_street_crew('Sunny')
  
#%% weather factor
def get_weather_factor(weather, rain=0, street_crew_working=False):
    if weather == 'Cloudy':
        weather_factor = 1.0 - rain / 100
    elif weather == 'Hot':
        weather_factor = 2.0
    else:
        if street_crew_working:
            weather_factor = 0.1
        else:   
            weather_factor = 1.0
    return weather_factor
# get_weather_factor('Cloudy')

#%% glasses sold
def get_glasses_sold(glasses_made, signs_made, price, weather_factor=1.0, storm=False, street_crew_working=False, street_crew_thirsty=False, meta=False):
    # constants
    price_factor_1 = 10
    price_factor_2 = 30
    sign_factor_1 = 0.5
    sign_factor_2 = 1
    # base units calc
    if price >= price_factor_1:
        base_demand = ((price_factor_1 ** 2) * price_factor_2 / price ** 2)
    else:
        base_demand = (price_factor_1 - price) / \
            price_factor_1 * 0.8 * price_factor_2 + price_factor_2
    # % increase in sales due to ads
    w = -signs_made * sign_factor_1
    sign_benefit = 1 - (math.exp(w) * sign_factor_2)
    # calculate adjusted units
    demand_multiplier = weather_factor * (1 + sign_benefit)
    demand = math.floor(demand_multiplier * base_demand)
    # special events
    if storm:
        demand = 0
    if street_crew_working:
        if street_crew_thirsty:
            demand = glasses_made
        else:
            demand = 0
    # calculate glasses sold
    glasses_sold = min(demand, glasses_made)
    if meta:
        return {'glasses_sold': glasses_sold, 'base_demand': base_demand,
                'sign_benefit': sign_benefit, 'demand_multiplier': demand_multiplier, 'demand': demand}
    else:
        return glasses_sold

# a = get_glasses_sold(glasses_made=80,price=9, signs_made=2,
#                  weather_factor=1.0, storm=False, street_crew_thirsty=False, meta=True)
# a['glasses_sold']

#%% cost per glass
def get_cost_per_glass(day=1):
    if day < 3:
        return 2
    elif day < 7:
        return 4
    else:
        return 5
# get_cost_per_glass(2)

#%% income, expenses, profit, and assets
def get_financials(glasses_made, signs_made, price, assets, glasses_sold, cost_per_glass, cost_per_sign=0.15):
    cost_per_sign = 0.15
    income = glasses_sold * price / 100    
    expenses = glasses_made * cost_per_glass / 100 + signs_made * cost_per_sign
    profit = income - expenses
    assets = assets + profit
    return income, expenses, profit, assets

# r= get_financials(glasses_made=10, signs_made=1, price=8, assets=2.00, glasses_sold=9,
#                cost_per_glass=.05, cost_per_sign=0.15)
# r

#%% main function
def get_ls_results(glasses_made, signs_made, price,
                day = 1, assets = 2.00, 
                weather=None, chance_of_rain=None, street_crew_working=None,
                street_crew_thirsty=None, storm=None, printresults=False):
    # calculate variables
    weather = weather or get_weather(day)
    chance_of_rain = chance_of_rain or get_chance_of_rain(weather)
    storm = storm or get_storm(weather)
    street_crew_working = street_crew_working or get_street_crew(weather)[0]
    street_crew_thirsty = street_crew_thirsty or get_street_crew(weather)[1]
    weather_factor = get_weather_factor(weather, chance_of_rain, street_crew_working)
    
    # calculate how many glasses are sold
    results = get_glasses_sold(glasses_made, signs_made, price, weather_factor, storm, street_crew_working, street_crew_thirsty, meta=True)
    glasses_sold = results['glasses_sold']
    cost_per_glass = get_cost_per_glass(day)
    cost_per_sign = 0.15
    income, expenses, profit, assets = get_financials(
        glasses_made, signs_made, price, assets, glasses_sold, cost_per_glass, cost_per_sign)

    # save results to dictionary
    d = {}
    d['Day'] = day
    d['Weather'] = weather
    d['GlassesMade'] = glasses_made  
    d['SignsMade'] = signs_made
    d['PricePerGlass'] = price
    d['WeatherFactor'] = weather_factor
    d['ChanceOfRain'] = chance_of_rain
    d['Storm'] = storm
    d['StreetCrewWorking'] = street_crew_working
    d['StreetCrewThirsty'] = street_crew_thirsty
    d['BaseDemand'] = results['base_demand']
    d['SignBenefit'] = results['sign_benefit']
    d['DemandMultiplier'] = results['demand_multiplier']
    d['AdjUnits'] = results['demand']
    d['GlassesSold'] = results['glasses_sold']
    d['CostPerGlass'] = cost_per_glass
    d['CostPerSign'] = cost_per_sign
    d['Income'] = income
    d['Expenses'] = expenses
    d['Profit'] = profit
    d['Assets'] = assets

    #return
    if printresults: # print results
        print('Day: ', d['Day'])
        print('Weather: ', d['Weather'])       
        print('PricePerGlass: ', d['PricePerGlass'])
        print('SignsMade: ', d['signs_madeMade'])
        print('GlassesMade: ', d['GlassesMade'])
        print('GlassesSold: ', d['GlassesSold'])
        print('Profit: ', d['Profit'])        
        print('Assets: ', d['Assets'])
        print('Storm: ', d['Storm'])        
        print('StreetCrewWorking: ', d['StreetCrewWorking'])
        print('StreetCrewThirsty: ', d['StreetCrewThirsty'])     
        print('WeatherFactor: ', d['WeatherFactor'])
        print('ChanceOfRain: ', d['ChanceOfRain'])
        print('BaseDemand: ', d['base_demand'])
        print('SignBenefit: ', d['sign_benefit'])
        print('DemandMultiplier: ', d['demand_multiplier'])
        print('AdjUnits: ', d['demand'])
        print('CostPerGlass: ', d['CostPerGlass'])
        print('CostPerSign: ', d['cost_per_sign'])
        print('Income: ', d['Income'])
        print('Expenses: ', d['Expenses'])
    else:  # return dictionary
        return d

#%% example day
# get_ls_results(glasses_made=70, signs_made=9, price=9,
#             day=1, assets=2.00,
#             weather=None, chance_of_rain=None, street_crew_working=None,
#             street_crew_thirsty=None, storm=None, printresults=False)
