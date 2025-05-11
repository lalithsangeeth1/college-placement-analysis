
# 📊 Government Treasury Expenditure Analysis - Visakhapatnam (April 2017-18)

## Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

## Step 2: Load the Dataset
df = pd.read_excel("visakhapatnam-district-treasury-expenditure---april-2017-18.xlsx", sheet_name="Expenditure")

## Step 3: Inspect and Clean the Data
# Drop fully empty columns
df = df.dropna(how='all', axis=1)

# Rename columns to snake_case
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Basic info
print(df.info())
print(df.head())

## Step 4: Exploratory Data Analysis

### A. Top 10 Expenditures
top10 = df.sort_values(by='amount', ascending=False).head(10)
print(top10[['amount', 'major_head_description', 'detailed_head_description']])

### B. Total Expenditure by Major Head
major_exp = df.groupby('major_head_description')['amount'].sum().sort_values(ascending=False).head(10)

sns.barplot(x=major_exp.values, y=major_exp.index, palette="viridis")
plt.title("Top 10 Major Head Expenditures")
plt.xlabel("Total Amount (INR)")
plt.ylabel("Major Head")
plt.show()

### C. Plan vs Non-Plan Expenditure
plan_split = df.groupby('plan/non_plan')['amount'].sum()

plan_split.plot(kind='pie', autopct='%1.1f%%', startangle=90, title='Plan vs Non-Plan Expenditure', ylabel="")
plt.show()

### D. Spending by Detailed Head
detailed_exp = df.groupby('detailed_head_description')['amount'].sum().sort_values(ascending=False).head(10)

sns.barplot(x=detailed_exp.values, y=detailed_exp.index, palette="coolwarm")
plt.title("Top 10 Detailed Head Expenditures")
plt.xlabel("Total Amount (INR)")
plt.ylabel("Detailed Head")
plt.show()

## Step 5: Summary Insights
# You can write textual conclusions or export these visuals as part of a report.
