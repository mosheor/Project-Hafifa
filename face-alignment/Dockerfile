COPY . /
USER root
WORKDIR /
RUN rpm -ivh /rpm/cmake-2.8.12.2-2.el7.x86_64.rpm && \
rpm -ivh /rpm/libXrender-0.9.10-5.fc28.x86_64.rpm
#RUN yum localinstall -y --skip-broken --nogpgcheck https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm && \
#yum localinstall -y --nogpgcheck http://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/e/epel-release-7-11.noarch.rpm && \
#yum localinstall -y --nogpgcheck http://rpms.famillecollet.com/enterprise/remi-release-7.rpm && \
#rpm --import https://www.elrepo.org/RPM-GPG-KEY-elrepo.org  && \
#rpm -Uvh http://www.elrepo.org/elrepo-release-7.0-3.el7.elrepo.noarch.rpm  && \
#yum localinstall -y --nogpgcheck http://repo.webtatic.com/yum/el7/webtatic-release.rpm
#RUN pip3 install /pipPackages/*
EXPOSE 5000
CMD ["echo", "hi there"]
#CMD ["python3", "/flask_server.py"]