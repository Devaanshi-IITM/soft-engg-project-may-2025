#!/bin/bash

set -e  # Exit on error

echo "⛴️ Starting Docker containers for FastAPI app..."

# Step 1: Build and start all services defined in docker-compose.yml
docker-compose up --build

echo "✅ All containers are up and running!"
