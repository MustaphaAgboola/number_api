#!/bin/bash

# Exit on error
set -e

# Update system packages
apt-get update
apt-get install -y python3-full python3-pip python3-venv git

# Create a directory for the application
mkdir -p /opt/number-api
cd /opt/number-api

# Clone the repository (replace with your repository URL)
git clone https://github.com/MustaphaAgboola/number_api.git .

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Set proper permissions
chown -R ubuntu:ubuntu /opt/number-api

# Create a systemd service file
cat > /etc/systemd/system/number-api.service << EOF
[Unit]
Description=Number API Flask Application
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/opt/number-api
Environment="PATH=/opt/number-api/venv/bin"
Environment="FLASK_APP=app.py"
Environment="FLASK_ENV=production"
ExecStart=/opt/number-api/venv/bin/python -m flask run --host=0.0.0.0 --port=5000
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Reload systemd and start service
systemctl daemon-reload
systemctl start number-api
systemctl enable number-api

# Check service status
systemctl status number-api

# Add logging
exec 1> >(logger -s -t $(basename $0)) 2>&1

echo "Deployment complete! Access the API at http://YOUR-EC2-IP:5000/number/12"