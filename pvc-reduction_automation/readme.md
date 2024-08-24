# pvc-reduction-automation

## Overview

This script operates in handles tasks such as generating YAML files, applying configurations, and managing data migration between PersistentVolumes.

## Script Behavior

- **Generate Files**: The script generates YAML files and JSON files necessary for StatefulSet and PersistentVolume management based on the namespace provided.
- **Apply Configurations**: It applies configurations for StatefulSets and PersistentVolumes.
- **Data Migration**:Migrate data between old and new PersistentVolumes.
- **Cleanup**: The script handles cleanup of old resources and ensures that new resources are applied correctly.

## Prerequisites

Ensure the following packages are installed:

1. **Python Packages**
   - PyYAML
     ```bash
     pip install PyYAML
     ```
   - Jinja2
     ```bash
     pip install Jinja2
     ```

2. **System Packages**
   - `jq`
     ```bash
     sudo apt-get install jq
     ```

## How to use :-

1. **Log in to the respective environment** (dev/prd/qa):
   - Ensure you are logged into the correct EKS environment where the script will be executed.

   - Change all the necessary paths in between the script [inside file_generator.py & main.sh]


2. **Run the Script**
   - Execute the script by running:
     ```bash
     ./main.sh
     ```

   - The script will prompt you to enter the namespace. It will then create a folder for the namespace and generate all necessary files within that folder.

   - After that it will ask you to validate all files that was created 

   - After selecting Yes , you can wait till the script completes

## Folder Structure

The script creates a folder in the following location:

- `buffering`: Contains template files for PV, PVC, and PVC migrator YAML.
- `historian`: Contains template files for PV, PVC, and PVC migrator YAML for historian.
- `data.csv`: Exported Excel file.
- `file_generator.py`: Creates PV,PVC,PVC migrator yaml files
- `sts_generatot.py`: Creates sts yaml files



---
