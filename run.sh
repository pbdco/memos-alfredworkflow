#!/bin/bash
set -e

# Add libs to Python path
export PYTHONPATH="./script/libs:$PYTHONPATH"

# Load environment variables
export $(cat .env | xargs)

# Run the script
python3 ./script/memos.py "$@" 