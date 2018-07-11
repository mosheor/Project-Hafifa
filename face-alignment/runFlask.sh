#!/usr/bin/env bash
#sudo docker kill FlaskServer
#sudo docker rm FlaskServer
#sudo docker image rm flask_server_image
sudo docker build -t flask_server_image .
sudo docker run -d -p 5000:5000 --name FlaskServer \
 -e OBJ_STORE_IP=172.17.0.2 \
 -e KEY_ID='1PU0GPZJPE62AEO3NOAD' \
 -e SECRET_KEY='U3MOCBYhyYRCZdKW4FaBM57A33aVnir63HcHdTAh' \
 flask_server_image