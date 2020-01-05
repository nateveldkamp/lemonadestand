#%% imports
import math
from random import random
#%% weather function
def get_weather():
    r = random()
    if r < 0.6: weather = 'Sunny' # 60% chance
    elif r < 0.8: weather = 'Cloudy' # 20% chance
    else: weather = 'Hot' # 20% chance
    return weather 

#%% simple demand function
def get_base_demand(price):
    return 20-price
price = 12
glasses_made = 10
demand = get_base_demand(price)
sales = min(demand, glasses_made)
print(f'{sales} glasses were sold.')
# Output: "8 glasses were sold."

#%% decision tree demand function
def get_demand_decision_tree(price, weather):
    if weather == 'Hot': demand = 30-price
    elif weather == 'Sunny': demand = 20-price
    else: demand = 10-price
    return demand
price = 8
glasses_made = 15
weather = get_weather()
demand = get_demand_decision_tree(price, weather)
sales = min(demand, glasses_made)
print(f'The weather is {weather}, demand is {demand}, and {sales} glasses were sold.')
# Output: "The weather is Sunny, demand is 12, and 12 glasses were sold."

#%% uplift demand function
def get_demand_uplift(price, weather):
    if weather == 'Hot': weather_factor=2.0    
    elif weather == 'Cloudy': weather_factor=.5
    else: weather_factor=1.0
    return weather_factor
price = 8
glasses_made = 15
weather = get_weather()
base_demand = get_base_demand(price)
demand_uplift = get_demand_uplift(price, weather)
demand = base_demand * demand_uplift
sales = min(demand, glasses_made)
print(f'The weather is {weather}, demand is {demand}, and {sales} glasses were sold.')
# Output: "The weather is Hot, demand is 24, and 15 glasses were sold."

#%% marketing uplift
def get_marketing_uplift(signs):
    return 1+(1-math.exp(-signs))

#%% customer class
class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def purchase(self, weather):
        r = random()
        purchase = False
        if weather == 'Hot': 
            if r<.8: purchase = True
        elif weather == 'Sunny': 
            if r<.6: purchase = True
        else: 
            if r<.3: purchase = True
        return purchase
#%% generate single customer
weather = get_weather()
customer = Customer("Nate", "male")
customer_purchase = 'did' if customer.purchase(weather) else 'did not'
print(f'The weather is {weather} and {customer.name} {customer_purchase} purchase')
#Output: The weather is Sunny and Nate did purchase

#%% generate multiple customers
customer_data = [
    {'name':'Bob', 'gender':'male'}, 
    {'name':'Alice', 'gender':'female'}, 
    {'name':'Mary', 'gender':'female'}
]
customers = [ Customer(i['name'], i['gender']) for i in customer_data ]
#%% results
weather = get_weather()
sales_results = [ [i.name, i.purchase(weather)] for i in customers]
sales = sum([i[1] for i in sales_results])
print(f'The weather is {weather} and demand is {sales}:')
for i in sales_results:
    name = i[0]
    purchase = 'did' if i[1] else 'did not'
    print(f'    {name} {purchase} purchase')
# Output:
# The weather is Sunny and demand is 2:
#     Bob did purchase
#     Alice did not purchase
#     Mary did purchase