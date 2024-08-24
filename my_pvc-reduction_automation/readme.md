#pvc-reduction

## Overview
It operates in WSL (Windows Subsystem for Linux) and handles tasks such as generating YAML files, applying configurations, and managing data migration between PersistentVolumes.

## Prerequisites

Ensure the following packages are installed:

1. **Python Packages**
   - PyYAML==6.0
     ```bash
     pip install PyYAML==6.0
     ```
   - Jinja2==3.1.2
     ```bash
     pip install Jinja2==3.1.2
     ```

2. **System Packages**
   - `jq`
     ```bash
     sudo apt-get install jq
     ```

3. **pip (Python Package Installer)**
   - Check if `pip` is installed:
     ```bash
     pip --version
     ```
   - If not installed, install `pip`:
     ```bash
     sudo apt-get install python3-pip
     ```

## Usage

1. **Log in to the respective environment** (dev/prd/qa):
   - Ensure you are logged into the correct EKS environment where the script will be executed.

2. **Run the Script**
   - Execute the script by running:
     ```bash
     ./main
     ```

   - The script will prompt you to enter the namespace. It will then create a folder for the namespace and generate all necessary files within that folder.

## Folder Structure

The script creates a folder in the following location:

- `buffering`: Contains template files for PV, PVC, and PVC migrator YAML.
- `historian`: Contains template files for PV, PVC, and PVC migrator YAML for historian.
- `data.csv`: Exported Excel file.

## Script Behavior

- **Generate Files**: The script generates YAML files and JSON files necessary for StatefulSet and PersistentVolume management based on the namespace provided.
- **Apply Configurations**: It applies configurations for StatefulSets and PersistentVolumes.
- **Data Migration**: It uses `rsync` to migrate data between old and new PersistentVolumes.
- **Cleanup**: The script handles cleanup of old resources and ensures that new resources are applied correctly.

