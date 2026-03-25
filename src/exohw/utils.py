import json

def load_json_file(filepath):
    """Reads and returns data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)