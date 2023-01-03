import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Import data
df = pd.read_csv("data/medical_examination.csv")


# Add 'overweight' column
df["overweight_num"] = df["weight"] / (df["height"] / 100) ** 2
df["overweight"] = np.where(df["overweight_num"] > 25, 1, 0)


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df["cholesterol"] = np.where(df["cholesterol"] > 1, 1, 0)
df["gluc"] = np.where(df["gluc"] > 1, 1, 0)


# Draw Categorical Plot:
# Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
df_cat = pd.melt(df, value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"], id_vars ="cardio")


# Draw the catplot with 'sns.catplot()'
plot = sns.catplot(data=df_cat, kind="count", x="variable", hue="value", col="cardio")
plot.set_axis_labels("", "total")
fig = plot.fig


# Draw Heat Map:
# Clean the data. Filter out patient segments that represent incorrect data.
df_heat = df[
(df["ap_lo"] <= df["ap_hi"]) & 
(df["height"] >= (df["height"].quantile(0.025))) &
(df["height"] <= (df["height"].quantile(0.975))) &
(df["weight"] >= (df["weight"].quantile(0.025))) &
(df["weight"] <= (df["weight"].quantile(0.975)))
]


# Calculate the correlation matrix
corr = df_heat.corr()


# Generate a mask for the upper triangle
mask = np.triu(corr)


# Set up the matplotlib figure
fig, ax = plt.subplots(figsize=(9,9))


# Draw the heatmap with 'sns.heatmap()'
sns.heatmap(corr,annot=True, fmt='.1f', linewidths=1, mask=mask, vmax=.8, center=0.09,square=True, cbar_kws = {'shrink':0.5})