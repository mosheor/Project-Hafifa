#!/usr/bin/env bash
sudo docker build -t flask_server_image .
sudo docker run -p 5000:5000 --name FlaskServer \
 -e OBJ_STORE_IP=172.17.0.3 \
 -e KEY_ID='1PU0GPZJPE62AEO3NOAD' \
 -e SECRET_KEY='U3MOCBYhyYRCZdKW4FaBM57A33aVnir63HcHdTAh' \
 -e MODEL_NAME='FaceAlignment.model' \
 flask_server_image