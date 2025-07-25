import os
import json

# The root directory of your project
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# The name of the output file
OUTPUT_FILE = 'full.json'

# Exclude the output file and the script itself from being processed
EXCLUDE_FILES = [OUTPUT_FILE, 'generate_json.py', 'api_server.py']

def generate_json_tree(directory):
    """
    Recursively generates a nested dictionary from the JSON files in a directory.
    """
    json_tree = {}
    # Exclude .git directory
    if ".git" in directory:
        return None

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)

        if item == '.git':
            continue

        if os.path.isdir(item_path):
            # Recursively process subdirectories
            subtree = generate_json_tree(item_path)
            if subtree: # Only add non-empty directories
                json_tree[item] = subtree
        elif item.endswith('.json') and item not in EXCLUDE_FILES:
            # Read the JSON data from the file
            try:
                # Check if the file is empty
                if os.path.getsize(item_path) < 2: # Check for less than 2 bytes to account for empty or near-empty files
                    print(f"Warning: Skipping empty or invalid file {item_path}")
                    continue
                
                with open(item_path, 'r', encoding='utf-8-sig') as f:
                    json_data = json.load(f)
                    # Use the filename without the .json extension as the key
                    json_tree[os.path.splitext(item)[0]] = json_data
            except json.JSONDecodeError:
                print(f"Warning: Could not decode JSON from {item_path}. Skipping.")
            except Exception as e:
                print(f"An error occurred while processing {item_path}: {e}")

    return json_tree

if __name__ == '__main__':
    # Generate the JSON tree starting from the root directory
    full_json_data = generate_json_tree(ROOT_DIR)

    # Write the combined JSON data to the output file
    output_path = os.path.join(ROOT_DIR, OUTPUT_FILE)
    with open(output_path, 'w') as f:
        json.dump(full_json_data, f, indent=4)

    print(f"Successfully generated {OUTPUT_FILE}")