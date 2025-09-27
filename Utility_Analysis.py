import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#Specify the column names given in the finalized dataset.
column_names = [
    "age", "workclass",  "education", 
     "occupation", "relationship", "race", "sex",
    "capital_gain", "capital_loss", "native_country", "income"
]
#Specify data path from the correct directory.
df = pd.read_csv("adult.data", header=None, names=column_names, na_values=" ?", skipinitialspace=True)

# Drop missing values
df = df.dropna()

# -----------------------------
# Encode categorical features, modern classifiers can automatically handle it.
# -----------------------------
categorical_cols = df.select_dtypes(include=["object"]).columns

label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# -----------------------------
# Split data
# -----------------------------
X = df.drop("income", axis=1)
y = df["income"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -----------------------------
# Train Random Forest
# -----------------------------
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# -----------------------------
# Evaluate accuracy
# -----------------------------
y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)

print(f"Accuracy on Adult dataset (Random Forest): {acc:.4f}")
