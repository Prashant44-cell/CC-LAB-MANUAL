#!/bin/bash
# Experiment 9: Running Containers from Docker Hub

echo "=== 1. Interactive Container (Ubuntu) ==="
docker container run -d --name ubuntu-test ubuntu top

echo "=== 2. Web Server Container (Nginx) ==="
docker container run --detach --publish 8080:80 --name nginx-app nginx

echo "=== 3. Database Container (MongoDB 4.4) ==="
docker container run --detach --publish 8081:27017 --name mongo-app mongo:4.4

echo "=== 4. Listing Running Containers ==="
docker container ls

echo "=== 5. Inspect Container Namespace ==="
docker container exec -it ubuntu-test ps -ef

echo "=== 6. Cleanup Containers ==="
docker container stop ubuntu-test nginx-app mongo-app
docker system prune -f
