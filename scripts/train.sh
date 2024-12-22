#!/bin/bash
# Train model script

echo "Running DVC pipeline to train the model..."

source venv/bin/activate
dvc repro train

echo "Model training complete!"
