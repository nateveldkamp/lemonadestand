#%% imports
# from lemonadestand import ls_day_results
#%% format dollars
def dformat(value, trim_zero=False):
    if value >= 0:
        string = '${:,.2f}'.format(value)
    else:
        string = '-${:,.2f}'.format(-value)
    if trim_zero and 1 > value > -1:
        string = string.replace('0', '', 1)
    return string

# input text
q3="""
YOUR EXPENSES ARE THE SUM OF THE COST OF
THE LEMONADE AND THE COST OF THE SIGNS.

YOUR PROFITS ARE THE DIFFERENCE BETWEEN
THE INCOME FROM SALES AND YOUR EXPENSES.

THE NUMBER OF GLASSES YOU SELL EACH DAY
DEPENDS ON THE PRICE YOU CHARGE, AND ON 
THE NUMBER OF ADVERTISING SIGNS YOU USE.

KEEP TRACK OF YOUR ASSETS, BECAUSE YOU 
CAN'T SPEND MORE MONEY THAN YOU HAVE!

 PRESS SPACE TO CONTINUE, ESC TO END...
"""
r_input_range = "COME ON, BE REASONABLE!!! TRY AGAIN."
r_input_range_2 = "COME ON, LET'S BE REASONABLE NOW!!! TRY AGAIN"
r_input_range_3 = "THINK AGAIN!!! YOU HAVE ONLY {} IN CASH AND TO MAKE {} GLASSES OF LEMONADE YOU NEED {} IN CASH.".format(2.00,100,20)
r_confirmation = "WOULD YOU LIKE TO CHANGE ANYTHING?"

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
    return"""
    $$ LEMONSVILLE DAILY FINANCIAL REPORT $$
       
       DAY {}                STAND {}

    {} GLASSES SOLD
    {} PER GLASS         INCOME {}

    {} GLASSES MADE
    {} SIGNS MADE      EXPENSES {}

                  PROFIT {}
                  ASSETS {}

    PRESS SPACE TO CONTINUE, ESC TO END... 
    """.format(day, stand, glasses_sold, price, income, glasses_made, signs_made, expenses, profit, assets)
# r = get_financial_report(day=1, glasses_made=8, signs_made=0, price=100, assets=.29,
#                          glasses_sold=8, income=0, expenses=.51, profit=-.51, stand=1)
# print(r)
#%% income, expenses, profit, and assets
def get_selection_header_txt(day, cost_per_glass, cost_per_glass_text, special_text, assets, stand=1):
    return"""-----------------------------------------
ON DAY {}, THE COST OF LEMONADE IS {}{}
{}
LEMONADE STAND {}      ASSETS {}""".format(day, cost_per_glass, cost_per_glass_text, special_text, stand, assets)

# r = get_selection_header_txt(day=1, cost_per_glass=.05, cost_per_glass_text="\n(THE PRICE OF LEMONADE MIX JUST WENT UP)",
#                  special_text="A HEAT WAVE IS PREDICTED FOR TODAY!", stand=1, assets=.29)
# print(r)
#%% input
print("""---------------------------------------
HI! WELCOME TO LEMONSVILLE, CALIFORNIA!
IN THIS SMALL TOWN, YOU ARE IN CHARGE OF
RUNNING YOUR OWN LEMONADE STAND. YOU CAN
COMPETE WITH AS MANY OTHER PEOPLE AS YOU
WISH, BUT HOW MUCH PROFIT YOU MAKE IS UP
TO YOU (THE OTHER STANDS' SALES WILL NOT
AFFECT YOUR BUSINESS IN ANY WAY). IF YOU
MAKE THE MOST MONEY, YOU'RE THE WINNER!!""")
while True:
    s_1 = input("\nARE YOU STARTING A NEW GAME? (YES OR NO)\nTYPE YOUR ANSWER AND HIT RETURN == >")
    if s_1 == "YES":
        break
    else:
        continue
while True:
    s_2 = int(input("HOW MANY PEOPLE WILL BE PLAYING ==> "))
    if s_2 == 1:
        break
    else:
        continue
s_3 = """---------------------------------------
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

PRESS SPACE TO CONTINUE, ESC TO END..."""
while True:
    input(s_3)
    break
s_4 = """---------------------------------------
YOUR EXPENSES ARE THE SUM OF THE COST OF
THE LEMONADE AND THE COST OF THE SIGNS.

YOUR PROFITS ARE THE DIFFERENCE BETWEEN
THE INCOME FROM SALES AND YOUR EXPENSES.

THE NUMBER OF GLASSES YOU SELL EACH DAY
DEPENDS ON THE PRICE YOU CHARGE, AND ON 
THE NUMBER OF ADVERTISING SIGNS YOU USE.

KEEP TRACK OF YOUR ASSETS, BECAUSE YOU 
CAN'T SPEND MORE MONEY THAN YOU HAVE!

PRESS SPACE TO CONTINUE, ESC TO END..."""
while True:
    input(s_4)
    break

while True:
    print(get_selection_header_txt(day=1, cost_per_glass=.05, cost_per_glass_text="",
                             special_text="", stand=1, assets=.29))
    try:
        glasses = int(input("\nHOW MANY GLASSES OF LEMONADE DO YOU\nWISH TO MAKE? "))
    except ValueError:
        while True:
            try:
                glasses = int(input("?REENTER \n"))
            except ValueError:
                continue
            else:
                break
    if 0 <= glasses > 100:
        print(r_input_range)
        continue
    else:
        break

while True:
    try:
        signs = int(input("\nHOW MANY ADVERTISING SIGNS ({} CENTS\nEACH) DO YOU WANT TO MAKE ? ".format(15)))
    except ValueError:
        while True:
            try:
                signs = int(input("?REENTER \n"))
            except ValueError:
                continue
            else:
                break
    if 0 <= signs > 100:
        print(r_input_range)
        continue
    else:
        break

while True:
    try:
        price = int(input("\nWHAT PRICE (IN CENTS) DO YOU WISH TO\nCHARGE FOR LEMONADE? "))
    except ValueError:
        while True:
            try:
                price = int(input("?REENTER \n"))
            except ValueError:
                continue
            else:
                break
    if 0 <= price > 100:
        print(r_input_range)
        continue
    else:
        break

print(glasses, signs, price)
# ls_day_results(glasses, signs, price,
#              day=1, assets=2.00,
#              weather=None, rain=None, crew=None,
#              thirsty=None, storm=None, printresults=True)



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
    return report
# get_weather_report('Cloudy',10,True)


#%% special event text
def get_special_event_text(street_crew_working):
    if street_crew_working:
        return "THE STREET DEPARTMENT IS WORKING TODAY. THERE WILL BE NO TRAFFIC ON YOUR STREET."
    else:
        return ""
# get_special_event_text(False)


#%% income, expenses, profit, and assets
"""
    DAY {}
    """.format(1)
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

#%% financial report
# def financial_report()
