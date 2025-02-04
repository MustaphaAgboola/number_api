#!/bin/bash

# Create a clean package folder
rm -rf package
mkdir package

# Install dependencies into package folder
pip install -r requirements.txt -t package

# Copy application code
cp -r app/* package/

# Zip the package
cd package || exit
zip -r ../deployment.zip .
cd ..

echo "Package created: deployment.zip"
