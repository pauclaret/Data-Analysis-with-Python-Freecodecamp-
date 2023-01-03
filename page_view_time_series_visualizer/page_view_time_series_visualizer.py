import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import calendar


# Import data
df = pd.read_csv("data/fcc-forum-pageviews.csv")


# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
n = 2.5
df_top = df.sort_values(by="value", ascending=False)
df_top = df_top.head(int(len(df)*(n/100)))
df_bottom = df.sort_values(by="value", ascending=True)
df_bottom = df_bottom.head(int(len(df)*(n/100)))
frames = [df, df_top, df_bottom]
df_cleaned = pd.concat(frames)
df_cleaned.drop_duplicates(keep=False, inplace=True)
df_cleaned['date'] = pd.to_datetime(df_cleaned['date'])


# Create a line plot using Matplotlib 
df_line = df_cleaned.copy()
df_line = df_line.set_index("date")

plt.plot(df_line["value"])
plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
plt.xlabel('Date')
plt.ylabel('Page Views')
plt.figure(figsize=(20,15))


# Create a bar plot. It should show average daily page views for each month grouped by year
df_bar = df_cleaned.copy()
df_bar['year'] = df_bar['date'].dt.year
df_bar['month'] = df_bar['date'].dt.month
df_bar['month_name'] = df_bar['month'].apply(lambda x: calendar.month_abbr[x])
df_bar = df_bar.sort_values(by=['month'])

sns.barplot(data=df_bar, y='value', x='year', hue='month_name', errorbar=None)
plt.xlabel('Years')
plt.ylabel('Average Page Views')
plt.legend(title="Months")


# Create two adjacent box plots using Seaborn. These box plots should show how the values are distributed within a given year or month and how it compares over time
df_box = df_bar.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]

fig, ax = plt.subplots(1,2,figsize=(15,5))
sns.boxplot(x=df_box["year"], y=df_box["value"], ax=ax[0]).set_title("Year-wise Box Plot (Trend)")
sns.boxplot(x=df_box["month"], y=df_box["value"], ax=ax[1]).set_title("Month-wise Box Plot (Seasonality)")
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Page Views')
ax[1].set_xlabel('Month')
ax[1].set_ylabel('Page Views')