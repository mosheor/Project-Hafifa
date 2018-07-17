#!/usr/bin/env bash
sudo docker build -t minio_image .
sudo docker run -p 9000:9000 --name minio \
minio_image