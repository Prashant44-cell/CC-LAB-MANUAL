# Python script to simulate cross-VM network socket file transfer

import socket

def send_file(filename, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        with open(filename, 'rb') as f:
            data = f.read(1024)
            while data:
                s.send(data)
                data = f.read(1024)
    print(f"File '{filename}' successfully sent to {host}:{port}")

if __name__ == "__main__":
    print("Cross-VM File Transfer Simulator Ready.")
