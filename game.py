#%% imports
from lemonadestand import *

intro_txt_1 ="""
---------------------------------------
HI! WELCOME TO LEMONSVILLE, CALIFORNIA!
IN THIS SMALL TOWN, YOU ARE IN CHARGE OF
RUNNING YOUR OWN LEMONADE STAND. YOU CAN
COMPETE WITH AS MANY OTHER PEOPLE AS YOU
WISH, BUT HOW MUCH PROFIT YOU MAKE IS UP
TO YOU (THE OTHER STANDS' SALES WILL NOT
AFFECT YOUR BUSINESS IN ANY WAY). IF YOU
MAKE THE MOST MONEY, YOU'RE THE WINNER!!"""
intro_txt_2 = """
ARE YOU STARTING A NEW GAME? (YES OR NO)
TYPE YOUR ANSWER AND HIT ENTER == >"""
intro_txt_3 = "HOW MANY PEOPLE WILL BE PLAYING ==> "
intro_txt_4 = """
---------------------------------------
TO MANAGE YOUR LEMONADE STAND, YOU WILL
NEED TO MAKE THESE DECISIONS EVERY DAY:

1. HOW MANY GLASES OF LEMONADE TO MAKE
  (ONLY ONE BATCH IS MADE EACH MORNING)
2. HOW MANY ADVERTISING SIGNS TO MAKE
  (THE SIGNS COST FIFTEEN CENTS EACH)

YOU WILL BEGIN WITH $2.00 CASH (ASSETS).
BECAUSE YOUR MOTHER GAVE YOU SOME SUGAR,
YOUR COST TO MAKE LEMONADE IS TWO CENTS
A GLASS (THIS MAY CHANGE IN THE FUTURE).

PRESS ENTER TO CONTINUE, ESC TO END..."""
intro_txt_5 = """
---------------------------------------
YOUR EXPENSES ARE THE SUM OF THE COST OF
THE LEMONADE AND THE COST OF THE SIGNS.

YOUR PROFITS ARE THE DIFFERENCE BETWEEN
THE INCOME FROM SALES AND YOUR EXPENSES.

THE NUMBER OF GLASSES YOU SELL EACH DAY
DEPENDS ON THE PRICE YOU CHARGE, AND ON 
THE NUMBER OF ADVERTISING SIGNS YOU USE.

KEEP TRACK OF YOUR ASSETS, BECAUSE YOU 
CAN'T SPEND MORE MONEY THAN YOU HAVE!

PRESS ENTER TO CONTINUE, ESC TO END..."""
intro_txt_6 = """
YOUR EXPENSES ARE THE SUM OF THE COST OF
THE LEMONADE AND THE COST OF THE SIGNS.

YOUR PROFITS ARE THE DIFFERENCE BETWEEN
THE INCOME FROM SALES AND YOUR EXPENSES.

THE NUMBER OF GLASSES YOU SELL EACH DAY
DEPENDS ON THE PRICE YOU CHARGE, AND ON 
THE NUMBER OF ADVERTISING SIGNS YOU USE.

KEEP TRACK OF YOUR ASSETS, BECAUSE YOU 
CAN'T SPEND MORE MONEY THAN YOU HAVE!

PRESS ENTER TO CONTINUE, ESC TO END...
"""

def intro():
  print(intro_txt_1)
  while True:
    i1 = input(intro_txt_2)
    if i1 == "YES":
        break
    else:
        continue
  while True:
    i2 = int(input(intro_txt_3))
    if i2 == 1:
        break
    else:
        continue
  while True:
    input(intro_txt_4)
    break
  while True:
    input(intro_txt_5)
    break

#%% selection header text
def get_selection_header_txt(day, cost_per_glass, cost_per_glass_text, special_text, assets, stand=1):
  txt = "\n-----------------------------------------"\
  "\nON DAY {}, THE COST OF LEMONADE IS {}{}"\
  "\n{}"\
  "\nLEMONADE STAND {}      ASSETS {}"\
  .format(day, cost_per_glass, cost_per_glass_text, special_text, stand, assets)
  print(txt)

# r = get_selection_header_txt(day=1, cost_per_glass=.05, cost_per_glass_text="\n(THE PRICE OF LEMONADE MIX JUST WENT UP)",
#                  special_text="A HEAT WAVE IS PREDICTED FOR TODAY!", stand=1, assets=.29)
# print(r)

#%% special event text
def get_special_event_text(street_crew_working):
    if street_crew_working:
        return "THE STREET DEPARTMENT IS WORKING TODAY. "\
        "THERE WILL BE NO TRAFFIC ON YOUR STREET."
    else:
        return ""

#%% special event text
def get_special_event_results_text(storm=False, crew_thirsty=False):
    if storm:
        return "ALL LEMONADE WAS RUINED."
    if crew_thirsty:
        return "THE STREET CREWS BOUGHT ALL YOUR LEMONADE AT LUNCHTIME!"
# get_special_event_results_text(storm=False, crew_thirsty=True)

#%% cost per glass text
def get_cost_per_glass_text(day=1):
    if day == 3:
        return "(YOUR MOTHER QUIT GIVING YOU FREE SUGAR)"
    elif day == 7:
        return "(THE PRICE OF LEMONADE MIX JUST WENT UP)"
    else:
        return ""
# get_cost_per_glass_text(2)

r_input_range = "\nCOME ON, BE REASONABLE!!! TRY AGAIN."
r_input_range_2 = "\nCOME ON, LET'S BE REASONABLE NOW!!! TRY AGAIN"
r_input_range_3 = "\nTHINK AGAIN!!! YOU HAVE ONLY {} IN CASH AND TO MAKE "\
"{} GLASSES OF LEMONADE YOU NEED {} IN CASH.".format(2.00,100,20)
r_confirmation = "WOULD YOU LIKE TO CHANGE ANYTHING?"

def get_user_input():
  while True:
    try:
      glasses = int(input("\nHOW MANY GLASSES OF LEMONADE DO YOU"\
      "\nWISH TO MAKE? "))
      if not 0 < glasses < 100:
        print(r_input_range)
        continue
      else:
        break
    except ValueError:
      print("\nOOPS!  THAT WAS NOT A VALID NUMBER.\nTRY AGAIN...")    
  while True:
    try:
      signs = int(input("\nHOW MANY ADVERTISING SIGNS ({} CENTS"\
      "\nEACH) DO YOU WANT TO MAKE ? ".format(15)))
      if not 0 < glasses < 100:
          print(r_input_range)
          continue
      else:
          break
    except ValueError:
      print("\nOOPS!  THAT WAS NOT A VALID NUMBER.\nTRY AGAIN...")
  while True:
    try:
      price = int(input("\nWHAT PRICE (IN CENTS) DO YOU WISH TO"\
      "\nCHARGE FOR LEMONADE? "))
      if not 0 < glasses < 100:
          print(r_input_range)
          continue
      else:
          break
    except ValueError:
      print("\nOOPS!  THAT WAS NOT A VALID NUMBER.\nTRY AGAIN...")         
  return glasses, signs, price

#%% format dollars
def dformat(value, trim_zero=False):
    if value >= 0:
        string = '${:,.2f}'.format(value)
    else:
        string = '-${:,.2f}'.format(-value)
    if trim_zero and 1 > value > -1:
        string = string.replace('0', '', 1)
    return string

#%% income, expenses, profit, and assets
def get_financial_report(day, glasses_made, signs_made, price, assets, glasses_sold, income, expenses, profit, stand=1):
    day = '{:<2d}'.format(glasses_sold)
    stand = '{:<2d}'.format(stand)
    glasses_sold = '{:^5}'.format(glasses_sold)
    price = '{:^5}'.format((dformat(price/100, True)))
    income = dformat(income)
    glasses_made = '{:^5}'.format(glasses_made)
    signs_made = '{:^5}'.format(signs_made)
    expenses = (dformat(expenses, True))
    profit = dformat(profit, True)
    assets = dformat(assets, True)
    txt = "---------------------------------------"\
    "\n$$ LEMONSVILLE DAILY FINANCIAL REPORT $$"\
    "\n"\
    "\n   DAY {}                STAND {}"\
    "\n"\
    "\n{} GLASSES SOLD"\
    "\n{} PER GLASS         INCOME {}"\
    "\n"\
    "\n{} GLASSES MADE"\
    "\n{} SIGNS MADE      EXPENSES {}"\
    "\n"\
    "\n              PROFIT {}"\
    "\n              ASSETS {}"\
    "\n"\
    "\nPRESS ENTER TO CONTINUE, ESC TO END..."\
    .format(day, stand, glasses_sold, price, income, glasses_made, signs_made, expenses, profit, assets)
    while True:
      input(txt)
      break

# r = get_financial_report(day=1, glasses_made=8, signs_made=0, price=100, assets=.29,
#                          glasses_sold=8, income=0, expenses=.51, profit=-.51, stand=1)
# print(r)
#%% income, expenses, profit, and assets

#%% weather report
def get_weather_report(weather, chance_of_rain=0, storm=False):
    if weather == 'Sunny':
        report = "SUNNY"
    elif storm == True:
        report = ("THUNDERSTORMS! \nA SEVERE THUNDERSTORM HIT LEMONSVILLE "
                  "EARLIER TODAY, JUST AS THE LEMONADE STANDS WERE BEING SET UP. "
                  "UNFORTUNATELY, EVERYTHONG WAS RUINED!")
    elif weather == 'Cloudy':
        report = ("CLOUDY \n" + "THERE IS A " + str(chance_of_rain) +
                  "% CHANSE OF LIGHT RAIN, AND THE WEATHER IS COOLER TODAY.")
    elif weather == 'Hot':
        report = "HOT AND DRY\nA HEAT WAVE IS PREDICTED FOR TODAY!"
    print("---------------------------------------"\
    "\n** LEMONSVILLE DAILY WEATHER REPORT **\n"\
    "\n{}".format(report))
# get_weather_report('Cloudy',10,True)

#%% financial report
# def financial_report()

def main():
  day = 1
  assets=2
  glasses_sold=3
  income=4
  expenses=5
  profit=6
  stand=1
  
  # intro()
 
  while True:
    #get daily weather and events
    weather = get_weather(day)
    chance_of_rain = get_chance_of_rain(weather)
    storm = get_storm(weather)
    street_crew_working = get_street_crew(weather)[0]
    street_crew_thirsty = get_street_crew(weather)[1]
    weather_factor = get_weather_factor(weather, chance_of_rain,street_crew_working)
    #get daily weather and events text output
    get_weather_report(weather, chance_of_rain, storm)
    special_event_text = get_special_event_text(street_crew_working)
    special_event_results_text = get_special_event_results_text(storm, street_crew_thirsty)
    cost_per_glass = get_cost_per_glass(day)
    cost_per_glass_text = get_cost_per_glass_text(day=1)
    special_text=""           
    selection_header_txt = get_selection_header_txt(day, cost_per_glass, cost_per_glass_text, special_text, assets, stand)
    #get user input
    glasses_made, signs_made, price = get_user_input()   
    #get daily business results
    marketing_factor = get_marketing_factor(signs_made)
    base_demand = get_base_demand(price)
    glasses_sold = get_glasses_sold(glasses_made, base_demand, weather_factor, marketing_factor, storm, street_crew_working, street_crew_thirsty)
    #get daily business results text
    get_financial_report(day, glasses_made, signs_made, price, assets, glasses_sold, income, expenses, profit, stand)
    break

main()