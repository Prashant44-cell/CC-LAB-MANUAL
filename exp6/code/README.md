# Experiment 6: VM File Transfer Procedures

## Aim:
To Find a procedure to transfer the files from one virtual machine to another virtual machine.

## Transfer Procedures:
1. **Shared Folders / Clipboard**: Enable Bidirectional Drag-and-Drop via Guest Additions.
2. **USB Passthrough**: Attach USB device under VM Settings -> USB after installing Extension Pack.
3. **Network File Transfer (SCP / SFTP)**: Configure Host-Only or Bridged Adapter and transfer via `scp`.
