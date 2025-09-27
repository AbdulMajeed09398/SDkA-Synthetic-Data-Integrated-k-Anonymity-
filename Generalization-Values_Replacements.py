import pandas as pd
import numpy as np

# Step 1: Read the already clustered data w.r.t. k-anonymity & l-diversity.
df = pd.read_csv('clustered_adult_data.csv')  
# In the below code, we will generalize the 'Age', 'Education', 'Workclass', and 'Sex' columns.
# The generalization process is the same for other attributes, just append the correct generalization.
# Some examples of the generalization are given in generalization_mappings.json for understanding.
# Generalize 'Age' into intervals, the interval can be adjusted as per the requirements.
df['age'] = pd.to_numeric(df['age'], errors='coerce')
df['age'].fillna(df['age'].mean(), inplace=True)  
# Generalize 'Age' into bins (make sure the column is numeric)
age_bins = list(range(0, 103, 2))  # Bin edges: [0, 3, 6, ..., 99, 102]
age_labels = [f'{i}-{i+3}' for i in range(0, 100, 2)] + ['100+']  # Labels for bins
# Apply binning to 'Age' column
df['Age Binned'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)
# Generalize 'Education' into broad categories
education_mapping = {
    'Bachelors': 'Undergraduate', 
    'Masters': 'Postgraduate', 
    'Doctorate': 'Postgraduate',
    'Assoc-acdm': 'Associate', 
    'Assoc-voc': 'Associate', 
    '10th': 'Junior-Secondry', 
    '11th': 'Senior-Secondry',
    '12th': 'Senior-Secondry', 
    'HS-grad': 'Senior-Secondry', 
    'Some-college': 'Undergraduate', 
    'Preschool': 'Other',
    '1st-4th': 'Elementry', 
    '5th-6th': 'Elementry', 
    '7th-8th': 'Elementry', 
    '9th': 'Junior-Secondry'  
}
df['Education Generalized'] = df['education'].map(education_mapping).fillna('Other')
workclass_mapping = {
    'Private': 'Private', 
    'Self-emp-not-inc': 'Self-Employed', 
    'Self-emp-inc': 'Self-Employed',
    'Federal-gov': 'Government', 
    'Local-gov': 'Government', 
    'State-gov': 'Government',
    'Without-pay': 'Others', 
    'Never-worked': 'Unemployed'
}
df['Workclass Generalized'] = df['workclass'].map(workclass_mapping).fillna('Others')
sex_mapping = {
    'Male': 'Male', 'Female': 'Female', 'Other': 'Other'  # This is just an example; modify as needed
}
df['Sex Generalized'] = df['sex'].map(sex_mapping).fillna('Other')

# Assuming 'Cluster ID' is the identifier for clusters
def apply_generalization_within_cluster(df, quasi_identifiers):
    # Read clusters & apply generalization
    anonymized_data = []
    for cluster_id, cluster_data in df.groupby('Cluster'):
        print(f"Processing Cluster ID: {cluster_id}")
        for column in quasi_identifiers:
            if cluster_data[column].nunique() == 1:
                # If there is only one unique value, skip the generalization for this column, later conver to real values also.
                #Uncomment to see results, if desirable. print(f"Skipping generalization for column '{column}' in Cluster ID {cluster_id} (only one unique value).")
                # Keep original value
                df.loc[cluster_data.index, column] = cluster_data[column]  
            else:
                # If there are multiple values, apply generalization.
                #Uncomment to see results, if desirable.print(f"Generalizing column '{column}' for Cluster ID {cluster_id}.")
                anonymized_data.append(cluster_data)
    # Combine anonymized data and add it to the DataFrame
    anonymized_df = pd.concat(anonymized_data, ignore_index=True)
    return anonymized_df

# Add labels for the generalized columns.
quasi_identifiers = ['Age Binned', 'Education Generalized', 'Workclass Generalized','Sex Generalized']
anonymized_df = apply_generalization_within_cluster(df,quasi_identifiers)
anonymized_df = anonymized_df[['Age Binned', 'Education Generalized', 'Workclass Generalized', 'Sex Generalized', 'income', 'Cluster']]
# Save results.
anonymized_df.to_csv('generalized_clustered_adult_data.csv', index=False)
