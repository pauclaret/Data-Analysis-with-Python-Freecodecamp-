import pandas as pd

# Read data from file
df = pd.read_csv("data/adult.data.csv")


# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = df["race"].value_counts()


# What is the average age of men?
df_age_men = df[df["sex"] == "Male"]
average_age_men = df_age_men["age"].mean()


# What is the percentage of people who have a Bachelor's degree?
df_bachelors = df["education"].value_counts(normalize=True) * 100
percentage_bachelors = df_bachelors["Bachelors"]


# What percentage of people have advanced education (Bachelors, Masters, or Doctorate)?
df_advanced = df["education"].value_counts(normalize=True) * 100
higher_education = df_advanced.loc[df_advanced.index.isin(["Bachelors", "Masters", "Doctorate"])].sum()


# What percentage of people do not have advanced education?
df_not_advanced = df["education"].value_counts(normalize=True) * 100
lower_education = df_not_advanced.loc[~df_not_advanced.index.isin(["Bachelors", "Masters", "Doctorate"])].sum()


# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
df_advanced_rich = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
higher_education_rich = df_advanced_rich["salary"].value_counts(normalize=True) * 100
percentage_higher_education_rich = higher_education_rich[">50K"]


# What percentage of people without advanced education make more than 50K?
df_not_advanced_rich = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
lower_education_rich = df_not_advanced_rich["salary"].value_counts(normalize=True) * 100
percentage_lower_education_rich = lower_education_rich[">50K"]


# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df["hours-per-week"].min()


# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min = df[df["hours-per-week"] == min_work_hours]
num_min_workers = len(num_min.index)

rich = num_min["salary"].value_counts(normalize=True) * 100
rich_percentage = rich[">50K"]


# What country has the highest percentage of people that earn >50K?
highest_earning = df[df['salary'] == '>50K']['native-country'].value_counts()
highest_earning_country = highest_earning.iloc[[0]]

highest_earning_country_p = (df[df['salary'] == ">50K"]['native-country'].value_counts() / df["native-country"].value_counts()*100).sort_values(ascending=False)
highest_earning_country_percentage = highest_earning_country_p.iloc[[0]]


# Identify the most popular occupation for those who earn >50K in India.
india_top = df[(df["salary"] == ">50K") & (df["native-country"] == "India")]
top_IN_occupation = india_top["occupation"].mode()

