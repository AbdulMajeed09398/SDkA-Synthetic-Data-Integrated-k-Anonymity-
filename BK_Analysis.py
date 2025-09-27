import pandas as pd
import numpy as np

# Step 1: Load the clustered data (Assume CSV file 'clustered_data.csv')
df = pd.read_csv('fused_clustered_adults_datak80.csv')

# Display the first few rows to understand the structure of the data
print(df.head())

# Step 2: Analyze the distribution of sensitive attributes within each cluster
sensitive_distribution = df.groupby(['Cluster', 'income']).size().unstack(fill_value=0)

# Print the sensitive attribute distribution within each cluster
print("Sensitive Attribute Distribution per Cluster:")
print(sensitive_distribution)

# Step 3: Assume the attacker knows the distribution of sensitive attributes
# For simplicity, assume the attacker knows that cluster 0 has 70% male, 30% female, etc.
# Based on this knowledge, we can perform the attack by inferring sensitive values.

# Let's simulate the attacker's action of inferring sensitive values:
# We'll assume that the attacker knows the distribution and guesses the most common value in each cluster.

# Step 4: Attack - Guess the sensitive attribute based on the distribution
predicted_sensitive_values = sensitive_distribution.idxmax(axis=1)  # This will pick the most frequent sensitive attribute for each cluster

# Step 5: Add these predictions as an additional column in the original DataFrame
df['predicted_sensitive_attribute'] = df['Cluster'].map(predicted_sensitive_values)

# Step 6: Compare predicted vs actual sensitive attribute values
correct_predictions = (df['income'] == df['predicted_sensitive_attribute']).sum()
total_predictions = df.shape[0]

# Calculate accuracy of the attack
accuracy = correct_predictions / total_predictions
print(f"Attack Accuracy: {accuracy:.2f}")

# Step 7: Output the result (e.g., how many individuals were correctly classified)
print(f"Correctly predicted sensitive attribute for {correct_predictions} out of {total_predictions} individuals.")
