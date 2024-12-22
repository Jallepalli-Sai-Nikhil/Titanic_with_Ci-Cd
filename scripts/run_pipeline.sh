#!/bin/bash
# Run full pipeline script

echo "Running full DVC pipeline..."

source venv/bin/activate
dvc repro

echo "Pipeline executed successfully!"
