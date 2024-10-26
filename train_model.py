import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
from huggingface_hub import HfApi, HfFolder


# iris = load_iris()
df = pd.read_csv("iris.csv")

# Assuming the last column is the target variable and the rest are features
X = df.iloc[:, :-1].values  # Features
y = df.iloc[:, -1].values    # Target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "model.pkl")