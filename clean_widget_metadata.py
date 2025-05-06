#!/usr/bin/env python3
import json
import sys

# Check if file name is provided
if len(sys.argv) < 2:
    print("Please provide a notebook file name")
    sys.exit(1)

notebook_file = sys.argv[1]

# Read the notebook
with open(notebook_file, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Fix the widget metadata
if 'metadata' in notebook:
    # Create a properly structured widgets metadata with both required keys
    notebook['metadata']['widgets'] = {
        'state': {},
        'application/vnd.jupyter.widget-state+json': {}
    }
    print(f"Updated widget metadata in {notebook_file}")
else:
    print(f"No metadata found in {notebook_file}")

# Write the notebook back
with open(notebook_file, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=2) 