#!/usr/bin/env bash
sudo -i
docker kill DjangoServer
docker rm DjangoServer
docker image rm DjangoServerImage
docker build -t DjangoServerImage .
docker run -d -p 8000:8000 --name DjangoServer -e OBJ_STORE_IP=172.17.0.2 -e FLASK_IP=0.0.0.0 DjangoServerImage