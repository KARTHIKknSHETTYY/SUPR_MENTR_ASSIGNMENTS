import pandas as pd

# load dataset 
data = pd.read_csv(r"C:\Users\karthik\Downloads\cars.csv")

# display top rows
print("Top 5 rows of dataset:")
print(data.head())

# find column with highest value
print("\nMaximum values in each column:")
print(data.max(numeric_only=True))

# count missing values
print("\nMissing values in each column:")
print(data.isnull().sum())