#!/usr/bin/env bash
sudo docker build -t django_server_image .
sudo docker run -p 8000:8000 --name DjangoServer \
-e OBJ_STORE_IP=172.17.0.2 \
-e FLASK_IP=172.17.0.3 \
-e KEY_ID='1PU0GPZJPE62AEO3NOAD' \
-e SECRET_KEY='U3MOCBYhyYRCZdKW4FaBM57A33aVnir63HcHdTAh' \
django_server_image