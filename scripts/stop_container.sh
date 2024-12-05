#!/bin/bash
set -e

# Stop and remove any running container that uses port 5000
echo "Stopping any container using port 5000..."

# Get the container ID that is using port 5000
container_id=$(docker ps -q -f "ancestor=sify12345/simple-python-flask-app" -f "publish=5000")

# If a container is running, stop and remove it
if [ -n "$container_id" ]; then
  echo "Stopping container $container_id..."
  docker stop $container_id
  docker rm $container_id
else
  echo "No container running on port 5000."
fi
