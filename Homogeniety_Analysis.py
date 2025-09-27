import pandas as pd

# Step 1: Read the clustered data from the CSV file
df = pd.read_csv('clustered_adults_datak10.csv')

# Step 2: Group data by cluster_id and check the unique values of the sensitive attribute
cluster_counts = df.groupby('Cluster')['income'].nunique()

# Step 3: Count how many clusters have only one unique value for the sensitive attribute
num_clusters_with_one_value = (cluster_counts == 1).sum()

# Step 4: Count the total number of unique clusters
total_clusters = df['Cluster'].nunique()

# Step 5: Print the results
print(f"Total number of clusters: {total_clusters}")
print(f"Number of clusters with one value for the sensitive attribute: {num_clusters_with_one_value}")
