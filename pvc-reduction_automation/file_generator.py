import csv
import yaml
import os
import sys
import json

# Define file paths for WSL
csv_path = "/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/data.csv"
output_dir_template = "/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/{namespace}"
buffering_folder_path = "/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/buffering"
historian_folder_path = "/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/historian"
#namespace = input("Enter your Namespace: ")
namespace = sys.argv[1]

output_dir = output_dir_template.format(namespace=namespace)
os.makedirs(output_dir, exist_ok=True)
data = []

# Read CSV and extract data
with open(csv_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header1 = next(csv_reader)  # Skip the headers
    header2 = next(csv_reader)  # Skip the headers
    
    for row in csv_reader:
        if row[0] == namespace:
            data_dict = {
                'node group': row[1],
                'availability zone': row[2],
                'volume-id': row[16],
                'pv-new': row[17],
                'pvc_new': row[18],
                'size': row[25],
                'application': row[14],
                'namespace': row[0]
            }
            data.append(data_dict)
json_data = json.dumps(data, indent=4)
print(f"-----------------------------Data captured from CSV-------------------------------:\n{json_data}")

# Manually extract the data from the JSON
extracted_data = [
    {
        "size": item["size"],
        "volume-id": item["volume-id"],
        "application": item["application"],
        "namespace": item["namespace"]
    }
    for item in data
]

# Save extracted data to a new JSON file
json_path = os.path.join(output_dir_template.format(namespace=namespace), 'size.json')
with open(json_path, 'w') as json_file:
    json.dump(extracted_data, json_file, indent=4)
    

# Function to replace placeholders in YAML files
def process_yaml_files(folders, item, output_dir):
    for folder in folders:
        if not os.path.isdir(folder):
            print(f"Folder not found: {folder}")
            continue
        for filename in os.listdir(folder):
            if filename.endswith('.yaml'):
                yaml_path = os.path.join(folder, filename)
                with open(yaml_path, 'r') as yaml_file:
                    yaml_content = yaml_file.read()
                
                # Replace placeholders in the YAML content
                for key, value in item.items():
                    placeholder = f'<{key}>'
                    yaml_content = yaml_content.replace(placeholder, value)
                
                # Save the updated YAML content to the namespace directory
                new_yaml_path = os.path.join(output_dir, filename)
                with open(new_yaml_path, 'w') as yaml_file:
                    yaml_file.write(yaml_content)
                
                #print(f"Updated YAML file saved to {new_yaml_path}")
                
# Process YAML files for each item in data
item=data[0]
process_yaml_files([buffering_folder_path], item, output_dir)
item=data[1]
process_yaml_files([historian_folder_path], item, output_dir)
