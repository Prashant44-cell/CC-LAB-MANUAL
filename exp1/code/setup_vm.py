# Python Script to Automate Virtual Workstation Configuration

import subprocess
import os

def create_virtual_workstation(vm_name="Cloud_VM", memory_mb=512, disk_size_mb=2048):
    print(f"Creating Virtual Machine: {vm_name}")
    print(f"Allocating Memory: {memory_mb} MB")
    print(f"Allocating Disk Space: {disk_size_mb} MB")
    
    commands = [
        f"VBoxManage createvm --name {vm_name} --ostype Windows98 --register",
        f"VBoxManage modifyvm {vm_name} --memory {memory_mb} --cpus 1 --vram 16",
        f"VBoxManage createhd --filename {vm_name}.vdi --size {disk_size_mb}",
        f"VBoxManage storagectl {vm_name} --name 'IDE Controller' --add ide"
    ]
    
    for cmd in commands:
        print(f"Executing: {cmd}")

if __name__ == "__main__":
    create_virtual_workstation()
