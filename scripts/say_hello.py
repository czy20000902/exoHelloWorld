"""
This module processes student enrollment data to generate personalized
greetings for individuals registered in a specific academic course
"""
import os
from exohw.utils import load_json_file
from types import SimpleNamespace

# Read students info from the json file
# Pillar: Data
people = load_json_file('data/raw/people.json')

# Read configs from the json file
# Pillar: Configuration
config_data = load_json_file('config/config.json')

# Map the configuration dictionary to a Namespace
# Pillar: Code / Configuration
cfg = SimpleNamespace(**config_data)

# Initialize an empty list to accumulate the generated greeting strings
# Pillar: Code
greetings = []

# Iterate through each record in the dataset to filter by course enrollment
# Pillar: Code / Data
for person in people:
    # Check if the target course string exists within the person's course list
    # Pillar: Code / Configuration
    if cfg.course in person[cfg.courses]:
        # Construct a greeting string using the person's name attribute
        # Pillar: Code / Configuration
        greetings.append(f"Hello {person[cfg.name]}\n")

# Retrieve the specific filesystem location for results from the system environment
# Pillar: Environment
output_dir = os.environ["OUTPUT_DIR"]

# Define the output path
# Pillar: Environment / Code
output_path = os.path.join(output_dir, 'greeting.txt')

# Create the output directory
# Pillar: Environment / Code
os.makedirs(output_dir, exist_ok=True)

# Open a file stream to write the results
# Pillar: Code / Environment
with open(output_path, 'w') as f:
    # Save the output into the target file
    # Pillar: Code / Data
    f.writelines(greetings)