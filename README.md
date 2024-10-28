# MLOPs-and-LLMOPs-Demo
A mini demo for demonstrate the basic steps of MLOPs using public tools and platforms, including dataset management, model training, CI/CD

## Prerequisites
Before starting with this project, ensure you have the following installed and configured:

1. **Python** (version 3.6 or higher)
   - Download and install Python from [python.org](https://www.python.org/).
   - Verify the installation by running:
     ```bash
     python --version
     ```

2. **Git** 

3. **VSCode**(recommended)

5. **Sign up for Hugging Face Hub Account**
   - Sign up at [huggingface.co](https://huggingface.co/)

6. **GitHub Account**
---

## Guidance
### 1. Fork and Clone this repo to your local machine
```bash
git clone git@github.com:Whynotmetoo/MLOPs-and-LLMOPs-Demo.git
```
### 2. Create virtual environment
```bash
python -m venv venv
```
### 3. Activate your virtual environment
* window:
```bash
venv\Scripts\activate
```
* Linux/macOS:
```bash
source venv/bin/activate
```
### 4. Install packages
```base
pip install -r requirements.txt
```
### 5. Run the code to train model
```bash
python train_model.py
```
### 6. Configure CI/CD
1.  Create Hugging Face Repo and access token
    - Creat a [new model repo](https://huggingface.co/new) and copy the repo id on the top left corner of the repo, in a format as `your_username/your_model_repo`
    - Go to **Settings > Access Tokens** to generate your token.
2. Create github repository secrets
    - Save the token as a **GitHub Secret** named `HF_TOKEN` and the repo id named `REPO_ID` in your GitHub repository for secure access during deployment. Go the **setting > Actions secrets and variables > Actions** to add your Repository secrets
### 7. push you code
push you code to github and check the pipeline