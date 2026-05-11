
import pandas as pd

# 1. Expanded Dataset
data = {
    "Company": ["Lockheed Martin", "Northrop Grumman", "General Dynamics", "RTX Corp", "L3Harris", "Huntington Ingalls", "Leidos", "Booz Allen", "SAIC", "CACI", "Howmet", "TransDigm", "HEICO", "AeroVironment", "Kratos", "BAE Systems", "Thales", "Leonardo", "Rheinmetall", "Honeywell", "Eaton", "Parker-Hannifin", "Teledyne", "Curtiss-Wright"],
    "Ticker": ["LMT", "NOC", "GD", "RTX", "LHX", "HII", "LDOS", "BAH", "SAIC", "CACI", "HWM", "TDG", "HEI", "AVAV", "KTOS", "BAESY", "HO.PA", "FINMY", "RNMBY", "HON", "ETN", "PH", "TDY", "CW"],
    "Current Price": [640, 725, 350, 205, 375, 290, 167, 150, 135, 370, 241, 1250, 200, 180, 22, 27, 160, 18, 75, 210, 330, 630, 430, 300],
    "52W High": [650, 730, 370, 205, 379, 293, 206, 170, 150, 400, 267, 1300, 210, 220, 25, 27, 165, 19, 80, 221, 345, 640, 450, 320],
    "52W Low": [420, 420, 240, 97, 160, 159, 135, 110, 105, 280, 160, 800, 150, 90, 12, 15, 110, 10, 40, 175, 192, 360, 350, 210]
}

df = pd.DataFrame(data)

# 2. Automated Calculations ("Finding stuff on its own")
df['52W Midpoint'] = (df['52W High'] + df['52W Low']) / 2
df['% off 52W High'] = (((df['52W High'] - df['Current Price']) / df['52W High']) * 100).round(2)
df['Annual Volatility ($)'] = df['52W High'] - df['52W Low']
df['Price Strength (%)'] = ((df['Current Price'] - df['52W Low']) / (df['52W High'] - df['52W Low']) * 100).round(1)

# 3. High-Level "Big Picture" Metrics
sector_avg_price = df['Current Price'].mean()
most_expensive = df.loc[df['Current Price'].idxmax(), 'Company']
closest_to_high = df.loc[df['% off 52W High'].idxmin(), 'Company']

# 4. Display Logic
print("="*100)
print(f"{'DEFENSE & AEROSPACE SECTOR ANALYSIS':^100}")
print("="*100)

# Formatting the output to be wider and more readable
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print(df.to_string(index=False))

print("-" * 100)
print(f"SECTOR SUMMARY:")
print(f"* Total Companies Analyzed: {len(df)}")
print(f"* Average Stock Price: ${sector_avg_price:.2f}")
print(f"* Highest Value Ticker: {most_expensive} (${df['Current Price'].max()})")
print(f"* Strongest Momentum: {closest_to_high} (only {df['% off 52W High'].min()}% off 52W High)")
print("-" * 100)

wb.save("top_25_defence_stocks.xlsx")
print("Stock table file created succesfully")









import pandas as pd

# Data from the provided image
data = {
    "Ticker": [
        "XOM", "CVX", "SHEL", "TTE", "BP", "COP", "EOG", "SLB", "HAL", 
        "PSX", "VLO", "MPC", "OXY", "DVN", "APA", "HES", "KMI", "WMB", 
        "PXD", "EQNR", "SU"
    ],
    "Current Price ($)": [
        120.3, 152.4, 73.5, 65.4, 38.5, 120.0, 128.0, 52.0, 38.0, 
        145.0, 155.0, 180.0, 65.0, 50.0, 32.0, 155.0, 18.5, 36.0, 
        240.0, 28.0, 38.0
    ],
    "52W Avg ($)": [
        110, 145, 68, 60, 35, 115, 120, 48, 35, 
        138, 148, 170, 60, 48, 30, 145, 17, 34, 
        230, 26, 35
    ],
    "52W High ($)": [
        122.6, 162.8, 76.3, 66.5, 40.2, 130.0, 140.0, 60.0, 42.0, 
        155.0, 170.0, 195.0, 72.0, 60.0, 38.0, 170.0, 20.0, 40.0, 
        260.0, 32.0, 42.0
    ],
    "52W Low ($)": [
        97.2, 129.2, 58.0, 49.5, 31.0, 95.0, 102.0, 42.0, 30.0, 
        120.0, 125.0, 150.0, 52.0, 40.0, 25.0, 120.0, 15.0, 30.0, 
        200.0, 22.0, None  # SU low was missing in the image
    ]
}

import pandas as pd

# 1. Setup the data
data = {
    "Ticker": ["XOM", "CVX", "SHEL", "TTE", "BP", "COP", "EOG", "SLB", "HAL", "PSX", "VLO", "MPC", "OXY", "DVN", "APA", "HES", "KMI", "WMB", "PXD", "EQNR", "SU"],
    "Current Price ($)": [120.3, 152.4, 73.5, 65.4, 38.5, 120.0, 128.0, 52.0, 38.0, 145.0, 155.0, 180.0, 65.0, 50.0, 32.0, 155.0, 18.5, 36.0, 240.0, 28.0, 38.0],
    "52W Avg ($)": [110, 145, 68, 60, 35, 115, 120, 48, 35, 138, 148, 170, 60, 48, 30, 145, 17, 34, 230, 26, 35],
    "52W High ($)": [122.6, 162.8, 76.3, 66.5, 40.2, 130.0, 140.0, 60.0, 42.0, 155.0, 170.0, 195.0, 72.0, 60.0, 38.0, 170.0, 20.0, 40.0, 260.0, 32.0, 42.0],
    "52W Low ($)": [97.2, 129.2, 58.0, 49.5, 31.0, 95.0, 102.0, 42.0, 30.0, 120.0, 125.0, 150.0, 52.0, 40.0, 25.0, 120.0, 15.0, 30.0, 200.0, 22.0, 30.0]
}

df = pd.DataFrame(data)

# 2. "Stuff" Python finds on its own (Row-level calculations)
# Calculate the Price Gap: How far the current price is from the 52W Average
df['Diff from Avg (%)'] = ((df['Current Price ($)'] - df['52W Avg ($)']) / df['52W Avg ($)'] * 100).round(2)

# Calculate the 52W Volatility Range (High - Low)
df['52W Range ($)'] = df['52W High ($)'] - df['52W Low ($)']

# 3. Automatic Statistical Summary
# This finds the Mean, Std Dev, Min, Max, and Percentiles for all columns
summary = df.describe().round(2)

print("--- FULL TABLE WITH CALCULATED COLUMNS ---")
print(df.to_string(index=False))

print("\n--- AUTOMATIC AVERAGES AND STATISTICS ---")

print(summary)






















# Create DataFrame
df = pd.DataFrame(data)

# Display the table
print(df.to_string(index=False))

# Optional: Save to CSV
# df.to_csv("energy_stocks.csv", index=False)

import datetime
import pytz

# Naive
# d = datetime.date(2001, 9, 11)

tday = datetime.date.today()


# weekday() - Monday is 0 and Sunday is 6
# print(tday)

# isoweekday() - Monday is 1 and Sunday is 7
# print(tday)


# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

tdelta = datetime.timedelta(hours=12)

# print(tday + tdelta)

# date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2016, 9, 24)

till_bday = bday - tday

# print(till_bday.days)

t = datetime.time(9, 30, 45, 100000)

# dt = datetime.datetime.today()
# dtnow = datetime.datetime.now()
# print(dir(datetime.datetime))
# print(dt)
# print(dtnow)

dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
# print(dir(dt))

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow2)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

dt_mtn = datetime.datetime.now()

mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)

# print(dt_mtn)

dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)

print(dt_mtn.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime - Datetime to String
# strptime - String to Datetime

	##Big Files:
	#f_contents = f.readlines()
	#print(f_contents)

    ###With the extra lines:
	#f_contents = f.readline()
	#print(f_contents)
	#f_contents = f.readline()
	#print(f_contents)

	###Without the extra lines:
	#f_contents = f.readline()
	#print(f_contents, end = '')
	#f_contents = f.readline()
	#print(f_contents, end = '')

	###Iterating through the file:
	#for line in f:
		#print(line, end = '')

	###Going Back....:
	#f_contents = f.read()
	#print(f_contents, end = '')

	###Printing by characters:
	#f_contents = f.read(100)
	#print(f_contents, end = '')
	#f_contents = f.read(100)
	#print(f_contents, end = '')
	#f_contents = f.read(100)
	#print(f_contents, end = '')

	###Iterating through small chunks:
	#size_to_read = 100
	#f_contents = f.read(size_to_read)
	#while len(f_contents) > 0:
		#print(f_contents)
		#f_contents = f.read(size_to_read)

	###Iterating through small chunks, with 10 characters:
	#size_to_read = 10
	#f_contents = f.read(size_to_read)
	#print(f_contents, end = '')
	#f.seek(0)
	#f_contents = f.read(size_to_read)
	#print(f_contents, end = '')
	#print(f.tell())
	#while len(f_contents) > 0:
		#print(f_contents, end = '*')
		#f_contents = f.read(size_to_read)
#print(f.mode)
#print(f.closed)
#print(f.read())


##Writing Files:
###The Error:
#with open("test.txt", "r") as f:

person = {'name': 'Jenn', 'age': 23}

# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)


# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print(sentence)


# sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
# print(sentence)


# tag = 'h1'
# text = 'This is a headline'

# sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)


sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
# print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(**person)
# print(sentence)

# for i in range(1, 11):
#     sentence = 'The value is {}'.format(i)
#     print(sentence)


# pi = 3.14159265

# sentence = 'Pi is equal to {}'.format(pi)

# print(sentence)


sentence = '1 MB is equal to {} bytes'.format(1000**2)

print(sentence)


import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

# print(my_date)

# March 01, 2016

sentence = '{:%B %d, %Y}'.format(my_date)

print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.

sentence = '{:%B %d, %Y} fell on a {} and was the {} day of the year'.format(my_date)

print(sentence)

nums = [1,2,3,4,5,6,7,8,9,10]

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
  my_list.append(n)
print my_list

print [n for n in nums]

# I want 'n*n' for each 'n' in nums
# my_list = []
# for n in nums:
#   my_list.append(n*n)
# print my_list

# Using a map + lambda
# my_list = map(lambda n: n*n, nums)
# print my_list

# I want 'n' for each 'n' in nums if 'n' is even
# my_list = []
# for n in nums:
#   if n%2 == 0:
#     my_list.append(n)
# print my_list

# Using a filter + lambda
# my_list = filter(lambda n: n%2 == 0, nums)
# print my_list

# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
# my_list = []
# for letter in 'abcd':
#   for num in range(4):
#     my_list.append((letter,num))
# print my_list

# Dictionary Comprehensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print zip(names, heros)

# I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print my_dict



# If name not equal to Peter

# Set Comprehensions
# nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
# my_set = set()
# for n in nums:
#     my_set.add(n)
# print my_set


# Generator Expressions
# I want to yield 'n*n' for each 'n' in nums
nums = [1,2,3,4,5,6,7,8,9,10]

# def gen_func(nums):
#     for n in nums:
#         yield n*n

# my_gen = gen_func(nums)

# for i in my_gen:
#     print i

