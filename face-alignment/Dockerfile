FROM fedora:28
COPY . /
USER root
RUN yum install -y python3-devel cmake && \
pip3.6 install /pipPackages/*
EXPOSE 5000
CMD ["python3", "/flask_server.py"]