#!/bin/bash
# Setup script

echo "Setting up the environment..."

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Initialize DVC
dvc init
dvc remote add -d myremote <REMOTE_STORAGE_URL>
dvc pull

# Setup Git
git init
git remote add origin <GITHUB_REPO_URL>
git pull origin main

echo "Setup complete!"
s