From minio/minio
ADD config.json /root/.minio/config.json
USER root
VOLUME /data
EXPOSE 9000/tcp
#CMD ["/usr/bin/docker-entrypoint.sh", "server", "/data"]
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]
CMD ["server","/data"]
