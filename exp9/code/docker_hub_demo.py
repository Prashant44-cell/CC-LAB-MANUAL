# Python script automating Docker Hub container deployment

import subprocess

def run_cmd(cmd):
    print(f"$ {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if res.stdout:
        print(res.stdout.strip())
    if res.stderr:
        print(res.stderr.strip())

if __name__ == "__main__":
    print("--- 1. Pulling and Running Ubuntu Container ---")
    run_cmd("docker run -d --name ubuntu_demo ubuntu top")
    
    print("
--- 2. Deploying Nginx Server ---")
    run_cmd("docker run -d -p 8080:80 --name nginx_demo nginx")
    
    print("
--- 3. Container Status ---")
    run_cmd("docker ps")
