import pandas as pd

# creating dataset
data = {
    "Study_Hours": [1,2,3,4,5,6,7,8],
    "Marks": [40,45,50,60,65,70,80,85]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)