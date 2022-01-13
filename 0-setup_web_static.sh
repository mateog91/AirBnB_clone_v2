#!/usr/bin/env bash
# This script is setting up your web servers for the deployment of web_static
# Install nginx
sudo apt-get -y update
sudo apt-get -y install nginx# Create directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# Create a fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
# Create a symbolic link
sudo ln -fs /data/web_static/releases/test/ /data/web_static/current# Give ownership
sudo chown -R ubuntu:ubuntu /data/
# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
file="/etc/nginx/sites-available/default"
sudo sed -i "/listen 80 default_server;/a \\\n\\tlocation /hbnb_static {\\n\\t\\talias /data/web_static/current/;\\n\\t}" $file# Restart server
sudo service nginx restart
