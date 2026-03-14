import numpy as np
from sklearn.linear_model import LinearRegression

# dataset (house size in sq ft vs price)
size = np.array([500, 800, 1000, 1200, 1500, 1800]).reshape(-1,1)
price = np.array([100000, 150000, 200000, 240000, 300000, 360000])

# train model
model = LinearRegression()
model.fit(size, price)

# predict price for new house
new_size = np.array([[1300]])
predicted_price = model.predict(new_size)

print("Predicted price for 1300 sq ft house:", predicted_price[0])