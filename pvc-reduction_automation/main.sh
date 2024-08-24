#!/bin/bash
read -p "Enter your Namespace: " namespace
python3 file_generator.py "$namespace"

if [ $? -eq 0 ]; then
    echo "------------------------PV & PVC Files are generated Successfull------------------------------------"
else
    echo "Something is Wrong !!!!!"
fi

buffering_yaml_file="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/sts-buffering-${namespace}.yaml"
buffering_yaml_new_file="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/sts-buffering-${namespace}-new.yaml"
historian_yaml_file="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/sts-historian-${namespace}.yaml"
historian_yaml_new_file="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/sts-historian-${namespace}-new.yaml"
pvc_migrator_buffering_yaml="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/pvc-migrator-buffering.yaml"
pvc_migrator_historian_yaml="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/pvc-migrator-historian.yaml"

# # Save StatefulSet YAML for buffering
kubectl get statefulset influxdb-buffering -n ${namespace} -o yaml > ${buffering_yaml_file}

# # Save StatefulSet YAML for historian
kubectl get statefulset influxdb-historian -n ${namespace} -o yaml > ${historian_yaml_file}

# Extract size from JSON file

size_json_file="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/size.json"
size_new_buffering=$(jq -r '.[] | select(.application == "influxdb-buffering") | .size' "${size_json_file}")
size_new_historian=$(jq -r '.[] | select(.application == "influxdb-historian") | .size' "${size_json_file}")

python3 sts-generator.py "$namespace" "$size_new_buffering" "$size_new_historian"

if [ $? -eq 0 ]; then
    echo "-----------------------------------------StatefulSet YAML files Generated successfully----------------------------"
else
    echo "Error occurred while modifying YAML files !!!!!"
    exit 1
fi

read -p "--------------------------------------Are all files validated ? (yes/no)------------------------------------------------: " confirmation

# Convert to lowercase for case-insensitive comparison
confirmation=$(echo "$confirmation" | tr '[:upper:]' '[:lower:]')

if [[ "$confirmation" == "yes" || "$confirmation" == "y" ]]; then
    echo "------------------------------Continuing with the script......................................."
else
    echo "Please correct the files and re-run the script."
    exit 1
fi

echo "---------------------------------------Applying PV-----------------------------------------------------"

pv_buffering_path="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/pv-buffering.yaml"
pv_historian_path="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/pv-historian.yaml"


kubectl apply -f "$pv_buffering_path"
kubectl apply -f "$pv_historian_path"

if [ $? -eq 0 ]; then
    echo "PV Applied successfully...."
else
    echo "Error occurred while applying PV !!!!!"
    exit 1
fi

echo "--------------------------------------PV Applied-------------------------------------------------------"

echo "---------------------------------------Applying PVC-----------------------------------------------------"

pvc_buffering_path="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/pvc-buffering.yaml"
pvc_historian_path="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/pvc-historian.yaml"

kubectl apply -f "$pvc_buffering_path"
kubectl apply -f "$pvc_historian_path"

if [ $? -eq 0 ]; then
    echo "PVC Applied successfully...."
else
    echo "Error occurred while applying PV !!!!!"
    exit 1
fi

echo "----------------------------------------PVC Applied--------------------------------------------------------"

echo "---------------------------------------Downtime Starts------------------------------------------------------"

echo "---------------------------------------Scaling Down STS------------------------------------------------------"

# Scale down influxdb-buffering StatefulSet
kubectl scale statefulset influxdb-buffering --replicas=0 -n "$namespace"

if [ $? -eq 0 ]; then
    echo "Successfully scaled down influxdb-buffering StatefulSet to 0 replicas."
else
    echo "Failed to scale down influxdb-buffering StatefulSet."
fi

# Scale down influxdb-historian StatefulSet
kubectl scale statefulset influxdb-historian --replicas=0 -n "$namespace"
if [ $? -eq 0 ]; then
    echo "Successfully scaled down influxdb-historian StatefulSet to 0 replicas."
else
    echo "Failed to scale down influxdb-historian StatefulSet."
fi


echo "------------------------------------Deploying PVC Migrator-----------------------------------------------------------------"

# Apply PVC Migrator for buffering

kubectl apply -f "$pvc_migrator_buffering_yaml"
if [ $? -eq 0 ]; then
    echo "Successfully applied pvc-migrator for buffering."
else
    echo "Failed to apply pvc-migrator for buffering."
fi

# Apply PVC Migrator for historian

kubectl apply -f "$pvc_migrator_historian_yaml"
if [ $? -eq 0 ]; then
    echo "Successfully applied pvc-migrator for historian."
else
    echo "Failed to apply pvc-migrator for historian."
fi

echo "---------------------------------Waiting for 30 sec till the pods come up----------------------------------------------------"

sleep 30

echo "---------------------------------Copying data from old PVC to new PVC---------------------------------------------------------"

# Define the PVC migrator pod names
buffering_pod_name="ubuntu-pvc-migrator-buffering"
historian_pod_name="ubuntu-pvc-migrator-historian"

# Check if the PVC migrator pod for buffering exists
buffering_pod=$(kubectl get pod "$buffering_pod_name" -n "$namespace" --no-headers -o custom-columns=":metadata.name")

if [ "$buffering_pod" != "$buffering_pod_name" ]; then
    echo "No pvc-migrator pod found for buffering with name $buffering_pod_name."
    exit 1
fi

echo "Found pvc-migrator pod for buffering: $buffering_pod"


# Copy data from old PVC to new PVC for buffering
kubectl exec -n "$namespace" "$buffering_pod" -- sh -c 'cp -a /mnt/old/. /mnt/new/'

# Check if the copy command was successful
if [ $? -eq 0 ]; then
    echo "Data copied successfully from /mnt/old to /mnt/new for buffering."
else
    echo "Failed to copy data from /mnt/old to /mnt/new for buffering."
    exit 1
fi

# Check if the PVC migrator pod for historian exists
historian_pod=$(kubectl get pod "$historian_pod_name" -n "$namespace" --no-headers -o custom-columns=":metadata.name")

if [ "$historian_pod" != "$historian_pod_name" ]; then
    echo "No pvc-migrator pod found for historian with name $historian_pod_name."
    exit 1
fi

echo "Found pvc-migrator pod for historian: $historian_pod"

# Copy data from old PVC to new PVC for historian
kubectl exec -n "$namespace" "$historian_pod" -- sh -c 'cp -a /mnt/old/. /mnt/new/'

# Check if the copy command was successful
if [ $? -eq 0 ]; then
    echo "Data copied successfully from /mnt/old to /mnt/new for historian."
else
    echo "Failed to copy data from /mnt/old to /mnt/new for historian."
    exit 1
fi

echo "-----------------------------------------Data Copy Complete----------------------------------"

echo "-----------------------------------------Deleting PVC Migrator Pods-------------------------------"

# Define the pod names
buffering_pod_name="ubuntu-pvc-migrator-buffering"
historian_pod_name="ubuntu-pvc-migrator-historian"

# Delete PVC migrator pod for buffering
echo "Deleting pvc-migrator pod for buffering: $buffering_pod_name"
kubectl delete pod "$buffering_pod_name" -n "$namespace"

if [ $? -eq 0 ]; then
    echo "Successfully deleted pvc-migrator pod for buffering."
else
    echo "Failed to delete pvc-migrator pod for buffering."
    exit 1
fi

# Delete PVC migrator pod for historian
echo "Deleting pvc-migrator pod for historian: $historian_pod_name"
kubectl delete pod "$historian_pod_name" -n "$namespace"

if [ $? -eq 0 ]; then
    echo "Successfully deleted pvc-migrator pod for historian."
else
    echo "Failed to delete pvc-migrator pod for historian."
    exit 1
fi

echo "------------------------------------Pod Deletion Complete---------------------------------------------"

echo "------------------------------------Deleting existing StatefulSet--------------------------------------"

# Define the StatefulSet names
buffering_sts_name="influxdb-buffering"
historian_sts_name="influxdb-historian"

# Delete StatefulSet for buffering
echo "Deleting StatefulSet for buffering: $buffering_sts_name"
kubectl delete statefulset "$buffering_sts_name" -n "$namespace"

if [ $? -eq 0 ]; then
    echo "Successfully deleted StatefulSet for buffering."
else
    echo "Failed to delete StatefulSet for buffering."
    exit 1
fi

# Delete StatefulSet for historian
echo "Deleting StatefulSet for historian: $historian_sts_name"
kubectl delete statefulset "$historian_sts_name" -n "$namespace"

if [ $? -eq 0 ]; then
    echo "Successfully deleted StatefulSet for historian."
else
    echo "Failed to delete StatefulSet for historian."
    exit 1
fi

echo "-------------------------StatefulSet Deletion Complete----------------------------------"


echo "-------------------------Applying new StatefulSet----------------------------------------"

# Define file paths for new StatefulSets
buffering_sts_new_file="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/sts-buffering-${namespace}-new.yaml"
historian_sts_new_file="/mnt/c/Users/SupriyoRoy/Desktop/pvc-reduction/${namespace}/sts-historian-${namespace}-new.yaml"

# Apply new StatefulSet for buffering
echo "Applying new StatefulSet for buffering: $buffering_sts_new_file"
kubectl apply -f "$buffering_sts_new_file"

if [ $? -eq 0 ]; then
    echo "Successfully applied new StatefulSet for buffering."
else
    echo "Failed to apply new StatefulSet for buffering."
    exit 1
fi

# Apply new StatefulSet for historian
echo "Applying new StatefulSet for historian: $historian_sts_new_file"
kubectl apply -f "$historian_sts_new_file"

if [ $? -eq 0 ]; then
    echo "Successfully applied new StatefulSet for historian."
else
    echo "Failed to apply new StatefulSet for historian."
    exit 1
fi

echo "-------------------------StatefulSet Application Complete--------------------------"

echo "--------------------------Scalling up sts------------------------------------------"

echo "Scaling the sts to 1"
# Scale down influxdb-buffering StatefulSet
kubectl scale statefulset influxdb-buffering --replicas=1 -n "$namespace"

if [ $? -eq 0 ]; then
    echo "Successfully scaled down influxdb-buffering StatefulSet to 1 replicas."
else
    echo "Failed to scale down influxdb-buffering StatefulSet."
fi

# Scale down influxdb-historian StatefulSet
kubectl scale statefulset influxdb-historian --replicas=1 -n "$namespace"
if [ $? -eq 0 ]; then
    echo "Successfully scaled down influxdb-historian StatefulSet to 1 replicas."
else
    echo "Failed to scale down influxdb-historian StatefulSet."
fi


echo "--------------------------Downtime Stopped------------------------------------------"
echo "--------------------------Activity Completed Successfull----------------------------"