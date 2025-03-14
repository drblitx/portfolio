"""
Codecademy Airline Analysis Practice Project
Emily Nover, March 2025
"""

# Importing modules
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels as sm
import matplotlib.pyplot as plt
import math

# Read in data
flight = pd.read_csv("/flight.csv")
print(flight.head())

# Univariate Analysis
"""
Task 1: What do coach ticket prices look like? What are the high and low values? "
"What would be considered the average? Does $500 seem like a good price for a coach ticket?
"""


"""
Task 2: Now visualize the coach ticket prices for flights that are 8 hours long. What are the high, 
low, and average prices for 8-hour-long flights? Does a $500 dollar ticket seem more reasonable than before?
"""


"""
Task 3: How are flight delay times distributed? Let's say there is a short amount of time between two connecting 
flights, and a flight delay would put the client at risk of missing their connecting flight. You want to better 
understand how often there are large delays so you can correctly set up connecting flights. What kinds of delays 
are typical?
"""


# Bivariate Analysis
"""
Task 4: Create a visualization that shows the relationship between coach and first-class prices. 
What is the relationship between these two prices? Do flights with higher coach prices always have higher 
first-class prices as well?
"""


"""
Task 5: What is the relationship between coach prices and inflight features &mdash; inflight meal, inflight 
entertainment, and inflight WiFi? Which features are associated with the highest increase in price?
"""


"""
Task 6: How does the number of passengers change in relation to the length of flights?
"""


# Multivariate Analysis
"""
Task 7: Visualize the relationship between coach and first-class prices on weekends compared to weekdays.
"""


"""
Task 8: How do coach prices differ for redeyes and non-redeyes on each day of the week?
"""