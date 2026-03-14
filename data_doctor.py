import pandas as pd

# load dataset
data = pd.read_csv(r"C:\Users\karthik\Downloads\cars.csv")
data.info()
# handle missing values (fill with column mean for numeric data)
data = data.fillna(data.mean(numeric_only=True))

# remove duplicate rows
data = data.drop_duplicates()

# standardize text (convert to lowercase)
data["brand"] = data["brand"].str.upper()

# display cleaned dataset
print("Cleaned Dataset:")
print(data.head())