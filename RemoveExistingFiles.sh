#!/bin/bash
yum update -y
yum install -y nginx
rm -rf /usr/share/nginx/html/index.html
service nginx start
