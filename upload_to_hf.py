from huggingface_hub import HfApi, HfFolder
import os

# Load your Hugging Face token from the environment variable
hf_token = HfFolder.get_token()
repo_id = os.getenv("REPO_ID")

# Initialize the API
api = HfApi()

# Define the model path and Hugging Face repository ID
model_path = "model.pkl"  # Path to your model file

# Get the current directory of this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the model path relative to the current directory
model_path = os.path.join(current_dir, "model.pkl")

# Upload the model to Hugging Face
api.upload_file(
    path_in_repo=model_path,
    path_or_fileobj=model_path,
    repo_type="model",
    repo_id=repo_id
)