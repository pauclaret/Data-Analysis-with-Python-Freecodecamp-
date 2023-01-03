import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from scipy import stats


# Read data from file
df = pd.read_csv("data/epa-sea-level.csv")


# Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050
x = df["Year"]
y = df["CSIRO Adjusted Sea Level"]

years_extended = np.arange(1880, 2051, 1)

res = stats.linregress(x, y)

line = [res.slope*xi + res.intercept for xi in years_extended]


# Plot a new line of best fit just using the data from year 2000 through the most recent year in the dataset. Make the line also go through the year 2050 to predict the sea level rise in 2050 if the rate of rise continues as it has since the year 2000
df_test = df.copy()
df_test = df_test.loc[df_test["Year"] > 1999]

x1 = df_test["Year"]
y1 = df_test["CSIRO Adjusted Sea Level"]

from_2000 = np.arange(2000, 2051, 1)

res1 = stats.linregress(x1, y1)

line1 = [res1.slope*xi + res1.intercept for xi in from_2000]


# Add labels and title
plt.plot(years_extended, line, color = 'orange', label="Fitting Line", linewidth=1)
plt.plot(from_2000, line1, color = 'red', label="Fitting Line", linewidth=1)
plt.scatter(x, y, s = 5, marker = '.', label="Sample Point", color = 'dodgerblue')
plt.title('Rise in Sea Level')
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')