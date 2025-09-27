import pandas as pd

# Step 1: Read the clustered data from the CSV file
df = pd.read_csv('clustered_adults_datak10.csv')

# Step 2: Count the occurrences of each sensitive value per cluster
sensitive_counts_per_cluster = df.groupby(['Cluster', 'income']).size().unstack(fill_value=0)

# Step 3: Calculate skewness of the sensitive attribute distribution across clusters
# We will use the skew() function to calculate the skewness of the distribution of each sensitive attribute
skewness = sensitive_counts_per_cluster.skew(axis=1, skipna=True)  # Skewness of each cluster

# Step 4: Compute the average skewness across all clusters
average_skewness = skewness.mean()

# Step 5: Print the results
print(f"Average skewness of sensitive attribute distribution across clusters: {average_skewness:.2f}")

# Optional: Output the skewness for each individual cluster
print("\nSkewness for each cluster:")
print(skewness)
