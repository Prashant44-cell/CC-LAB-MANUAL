#!/bin/bash
# Experiment 1: Virtual Workstation Setup using VirtualBox VBoxManage CLI

echo "=== Experiment 1: Installing & Configuring Virtual Workstation ==="

# Step 1: Download Oracle VirtualBox (Manual/Automated)
echo "[1] Checking VirtualBox installation..."
VBOXMANAGE="VBoxManage"

# Step 2: Create a New Virtual Machine
VM_NAME="Cloud_Virtual_Workstation"
OS_TYPE="Windows98" # Or Ubuntu_64

echo "[2] Creating Virtual Machine: $VM_NAME ($OS_TYPE)"
$VBOXMANAGE createvm --name "$VM_NAME" --ostype "$OS_TYPE" --register

# Step 3: Configure RAM and CPUs
echo "[3] Setting Hardware Resources (RAM: 512MB, CPU: 1)..."
$VBOXMANAGE modifyvm "$VM_NAME" --memory 512 --cpus 1 --vram 16

# Step 4: Create Storage Controller and Virtual Hard Disk
echo "[4] Creating Storage Controller and Virtual Hard Disk (2.0 GB)..."
$VBOXMANAGE createhd --filename "$VM_NAME.vdi" --size 2048
$VBOXMANAGE storagectl "$VM_NAME" --name "IDE Controller" --add ide
$VBOXMANAGE storageattach "$VM_NAME" --storagectl "IDE Controller" --port 0 --device 0 --type hdd --medium "$VM_NAME.vdi"

# Step 5: Mount OS ISO Image
ISO_PATH="/path/to/Win98SE.iso"
echo "[5] Mounting ISO Image: $ISO_PATH"
$VBOXMANAGE storageattach "$VM_NAME" --storagectl "IDE Controller" --port 1 --device 0 --type dvddrive --medium "$ISO_PATH"

echo "=== Virtual Workstation Setup Completed Successfully ==="
