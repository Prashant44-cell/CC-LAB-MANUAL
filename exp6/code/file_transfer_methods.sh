#!/bin/bash
# Experiment 6: File Transfer Procedures Between Virtual Machines

echo "=== File Transfer Methods Between Virtual Machines ==="

# Method 1: VirtualBox Drag-and-Drop & Shared Clipboard
# Devices -> Drag and Drop -> Bidirectional
# Devices -> Shared Clipboard -> Bidirectional

# Method 2: USB Drive Passthrough
# 1. Install VirtualBox Extension Pack.
# 2. Add current user to vboxusers group:
sudo usermod -aG vboxusers $USER
# 3. Mount USB in VirtualBox Settings -> USB -> Add Device.

# Method 3: Network Shared Folder / SCP Command
echo "[3] Transferring file via Secure Copy Protocol (SCP):"
SOURCE_FILE="experiment_data.txt"
TARGET_VM_USER="ubuntu"
TARGET_VM_IP="192.168.56.102"
DEST_PATH="/home/ubuntu/"

scp $SOURCE_FILE $TARGET_VM_USER@$TARGET_VM_IP:$DEST_PATH
