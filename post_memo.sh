#!/bin/bash
set -e

# Add libs to Python path
export PYTHONPATH="./libs:$PYTHONPATH"

# Load environment variables
export $(cat .env | xargs)

# Pass all arguments to the Python script
python3 memos.py "$@" 