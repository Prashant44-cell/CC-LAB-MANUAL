#!/bin/bash
# Experiment 8: Docker Container Creation & Execution

echo "=== Building Docker Image ==="
docker build -t python-test .

echo "=== Running Docker Container ==="
docker run python-test
