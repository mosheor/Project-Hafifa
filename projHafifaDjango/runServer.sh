#!/usr/bin/env bash
sudo docker build -t django_server_image .
sudo docker run -d -p 8000:8000 --name DjangoServer -e OBJ_STORE_IP=172.17.0.2 -e FLASK_IP=0.0.0.0 django_server_image