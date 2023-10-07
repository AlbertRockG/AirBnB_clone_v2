#!/usr/bin/env bash
# Sets up my web servers for the deployment of web_static.
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo '<html>
  <head>
  </head>
  <body>
    Hello, World!
  </body>
</html>' > /data/web_static/releases/test/inded.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {

    listen 80 default_server;
    listen [::]:80 default server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
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
}" > /etc/nginx/sites-available/default

if [ "$(pgrep -c nginx)" -le 0 ]; then
    service nginx start
else 
    service nginx restart
fi