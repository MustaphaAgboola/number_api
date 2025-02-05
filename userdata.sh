#!/bin/bash

# Update system packages
sudo apt update -y && sudo apt upgrade -y

# Install required packages
sudo apt install -y python3 python3-pip git

# Create a project directory
mkdir -p /home/ubuntu/flask_app
cd /home/ubuntu/flask_app

# Clone your Flask app (Replace with your GitHub repo)
git clone https://github.com/MustaphaAgboola/number_api.git .


# Install dependencies
pip3 install -r requirements.txt

# Start the Flask app using Gunicorn (Change `main:app` based on your Flask file)
gunicorn --workers 3 --bind 0.0.0.0:5000 main:app --daemon

# Configure firewall to allow traffic on port 5000
sudo ufw allow 5000

# Enable firewall
sudo ufw enable -y

# Create a systemd service to ensure Flask runs on reboot
sudo bash -c 'cat <<EOF > /etc/systemd/system/flask.service
[Unit]
Description=Gunicorn instance to serve Flask API
After=network.target

[Service]
User=ubuntu
Group=ubuntu
WorkingDirectory=/home/ubuntu/flask_app
ExecStart=/usr/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 main:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF'

# Reload systemd and enable the Flask service
sudo systemctl daemon-reload
sudo systemctl enable flask
sudo systemctl start flask

# Print a message
echo "Flask app is running on EC2 at port 5000!"
