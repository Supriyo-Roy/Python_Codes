import yaml
import sys
import os

def modify_statefulset(input_file, output_file, size_new):
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} does not exist.")
        sys.exit(1)

    try:
        with open(input_file, "r") as file:
            data = yaml.safe_load(file)
    except yaml.YAMLError as exc:
        print(f"Error reading YAML file: {exc}")
        sys.exit(1)

    # Check if keys exist before accessing them
    containers = data.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])
    init_containers = data.get("spec", {}).get("template", {}).get("spec", {}).get("initContainers", [])
    volume_claim_templates = data.get("spec", {}).get("volumeClaimTemplates", [])

    # Modify containers and initContainers
    for container in containers:
        if container.get("image", "").startswith("art.pmideep.com/icloud-docker-prod/ic-data/influxdb"):
            for mount in container.get("volumeMounts", []):
                if mount.get("name") == "influxdb-buffering-storage":
                    mount["name"] = "influxdb-buffering-storage-new"
                elif mount.get("name") == "influxdb-historian-storage":
                    mount["name"] = "influxdb-historian-storage-new"
        elif container.get("image", "").startswith("art.pmideep.com/icloud-docker-prod/pod-diskusage"):
            for mount in container.get("volumeMounts", []):
                if mount.get("name") == "influxdb-buffering-storage":
                    mount["name"] = "influxdb-buffering-storage-new"
                elif mount.get("name") == "influxdb-historian-storage":
                    mount["name"] = "influxdb-historian-storage-new"

    for init_container in init_containers:
        if init_container.get("image", "").startswith("busybox"):
            for mount in init_container.get("volumeMounts", []):
                if mount.get("name") == "influxdb-buffering-storage":
                    mount["name"] = "influxdb-buffering-storage-new"
                elif mount.get("name") == "influxdb-historian-storage":
                    mount["name"] = "influxdb-historian-storage-new"

    # Modify volumeClaimTemplates
    for vct in volume_claim_templates:
        if vct.get("metadata", {}).get("name") == "influxdb-buffering-storage":
            vct["metadata"]["name"] = "influxdb-buffering-storage-new"
            vct["spec"]["resources"]["requests"]["storage"] = f"{size_new}Gi"
        elif vct.get("metadata", {}).get("name") == "influxdb-historian-storage":
            vct["metadata"]["name"] = "influxdb-historian-storage-new"
            vct["spec"]["resources"]["requests"]["storage"] = f"{size_new}Gi"

    try:
        with open(output_file, "w") as file:
            yaml.dump(data, file)
    except IOError as exc:
        print(f"Error writing YAML file: {exc}")
        sys.exit(1)

def main():
    if len(sys.argv) != 4:
        print("Usage: python sts-generator.py <namespace> <size_new_buffering> <size_new_historian>")
        sys.exit(1)

    namespace = sys.argv[1]
    size_new_buffering = sys.argv[2]
    size_new_historian = sys.argv[3]

    # Check if size_new_buffering and size_new_historian are integers
    try:
        int(size_new_buffering)
        int(size_new_historian)
    except ValueError:
        print("Error: Size values must be integers.")
        sys.exit(1)

    # Modify buffering StatefulSet
    modify_statefulset(
        f"/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/{namespace}/sts-buffering-{namespace}.yaml",
        f"/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/{namespace}/sts-buffering-{namespace}-new.yaml",
        size_new_buffering
    )

    # Modify historian StatefulSet
    modify_statefulset(
        f"/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/{namespace}/sts-historian-{namespace}.yaml",
        f"/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/{namespace}/sts-historian-{namespace}-new.yaml",
        size_new_historian
    )

if __name__ == "__main__":
    main()
