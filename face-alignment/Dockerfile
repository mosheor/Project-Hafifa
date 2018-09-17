FROM registry.access.redhat.com/rhscl/python-36-rhel7
COPY . /
USER root
WORKDIR /
RUN subscription-manager register --username=---- --password=---- && \
subscription-manager attach --auto
RUN yum install -y cmake python3-devel libXext libSM libXrender
# gcc gcc-c++ make zlib-devel openssl \
#openssl-devel  && \
RUN pip3.6 install /pipPackages/*
EXPOSE 5000
#CMD ["echo", "hi there"]
CMD ["python3.6", "/flask_server.py"]
