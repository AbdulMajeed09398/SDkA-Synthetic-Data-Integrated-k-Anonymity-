import pandas as pd

# Step 1: Load the clustered data (Assume CSV file 'clustered_data.csv')
df = pd.read_csv('fused_clustered_adults_datak10.csv')

# Display the first few rows of the dataset
print("Clustered Data:")
print(df.head())

# Step 2: Assume the attacker has some background knowledge of age, sex, education, workclass, and income
# Example of background knowledge (This would be some external database or public information)
external_knowledge = pd.DataFrame({
    'age': [32, 30, 45, 32, 46],
    'workclass': ['Private', 'Federal-gov', 'Private', 'Local-gov', 'Private'],
    'education': ['Some-college', 'Bachelors', 'PhD', 'HS-grad', 'PhD'],
    'sex': ['Female', 'Male', 'Male', 'Female', 'Male'],
    'occupation': ['Sales', ' Prof-specialty', ' Craft-repair', 'Sales', ' Tech-support'],
    'real_identity': ['Person_A', 'Person_B', 'Person_C', 'Person_D', 'Person_E']
})

# Step 3: Ensure that the data types of the columns are consistent (e.g., 'age' should be the same type)
# Cast 'age' column in external_knowledge to int64 to match the type in df
external_knowledge['age'] = external_knowledge['age'].astype('int64')
df['age'] = pd.to_numeric(df['age'], errors='coerce')
external_knowledge['age'] = pd.to_numeric(external_knowledge['age'], errors='coerce')

# Step 4: Link the clustered data to real-world identities using background knowledge
# Perform a merge between the clustered data and external knowledge based on common attributes
linked_data = pd.merge(df, external_knowledge, on=['age', 'workclass',  'education','sex', 'income'], how='left')

# Step 5: Assess the success of the linking attack
# If we were able to link individuals, it means we have successfully re-identified them
successful_links = linked_data[linked_data['real_identity'].notnull()]

# Step 6: Output the results
print("\nLinked Data:")
print(successful_links[['Cluster', 'age', 'workclass', 'education','sex',  'income', 'real_identity']])

# Number of successfully linked individuals
successful_count = len(successful_links)
print(f"\nNumber of successfully linked individuals: {successful_count}")
