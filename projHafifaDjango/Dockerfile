FROM registry.access.redhat.com/rhscl/python-36-rhel7
COPY . /
WORKDIR /
RUN pip3.6 install /pipPackages/*
EXPOSE 8000
CMD ["python3.6", "/manage.py", "runserver", "0.0.0.0:8000"]