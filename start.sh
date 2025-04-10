#!/bin/bash

# Copy React build to FastAPI public directory
# cp -r react/out/* fastapi/public/

# Copy production config to FastAPI config
cp fastapi/config-prod.py fastapi/config.py

# Start FastAPI server
fastapi run fastapi/main.py