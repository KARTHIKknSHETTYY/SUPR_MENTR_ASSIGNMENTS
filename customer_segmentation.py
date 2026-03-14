import pandas as pd
from sklearn.cluster import KMeans

# load dataset
data = pd.read_csv(r"C:\Users\karthik\Downloads\Mall_Customers.csv")

# selecting features (example: annual income and spending score)
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]

# apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
data['Cluster'] = kmeans.fit_predict(X)

print(data.head())