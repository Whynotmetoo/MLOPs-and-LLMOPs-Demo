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
# X = iris.data
# y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, "model.pkl")

# Login to Hugging Face
# HfFolder.save_token('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')

# api = HfApi()
# api.upload_model(model_dir="model.pkl", repo_id="CarlsonYeh223/test-model")
# api.upload_file(
#     path_in_repo="model.pkl",
#     path_or_fileobj="D:\Courses\SE Studio\MLOPs-and-LLMOPs-Demo\model.pkl",
#     repo_type="model",
#     repo_id="CarlsonYeh223/test-model"
# )