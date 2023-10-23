#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static.
sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "Hello, World!" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

nginx_config="server {

    listen *:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://cuberrule.com/;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}"

echo "$nginx_config" | sudo tee /etc/nginx/conf.d/default.conf
sudo rm -rf /etc/nginx/sites-enabled/default
if sudo nginx -t; then # Check Nginx configuration
    sudo service nginx reload
else
    echo "nginx config failed!"
fi
