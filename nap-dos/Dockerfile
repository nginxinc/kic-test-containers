FROM ubuntu:bionic
ENV NOTVISIBLE "in users profile"
RUN set -x \
  && apt-get update \
  && apt-get -yq install linux-headers-4.15.0-51-generic \
  && apt-get install -y python3 \
  && apt-get -yq install build-essential \
  && apt-get -yq install freeradius \
  && apt-get -yq install freeradius-utils \
  && apt-get -yq install libssl-dev \
  && apt-get -yq install python-openssl \
  && apt-get -yq install python3-pip \
  && pip3 install --no-cache-dir --upgrade pip \
  && hash -r pip \
  && apt-get -yq install openssh-server \
  && apt-get -yq install libffi-dev \
  && apt-get -yq install git \
  && git config --global http.sslVerify false \
  && apt-get -yq install vim-tiny \
  && apt-get -yq install iputils-ping \
  && apt-get -yq install iproute2 \
  && apt-get -yq install iptables \
  && apt-get -yq install libmysqlclient-dev \
  && apt-get -yq install tcpreplay \
  && apt-get -yq install psmisc \
  && DEBIAN_FRONTEND=noninteractive apt-get -yq install hping3 \
  && pip3 install scapy==2.4.0 \
  && pip3 install configparser==3.5.0 \
  && pip3 install python-iptables==0.14.0 \
  && pip3 install polling==0.3.0 \
  && pip3 install pyopenssl==16.2.0 \
  && pip3 install pytest==5.4.1 \
  && pip3 install pytest-timeouts==1.2.1 \
  && pip3 install pytest-repeat \
  && pip3 install pytest-ordering \
  && pip3 install pytest-assume==2.2.1 \
  && pip3 install pytest-lazy-fixture==0.6.3 \
  && pip3 install locustio==0.14.6 \
  && pip3 install psutil \
  && pip3 install flask \
  && pip3 install Flask-RESTful>=0.3.6 \
  && pip3 install requests>=2.12.4 \
  && pip3 install PyYAML==3.13 \
  && pip3 install gunicorn \
  && pip3 install pyyml==0.0.2 \
  && pip3 install pyroute2 \
  && pip3 install pyvmomi \
  && pip3 install xmltodict
RUN apt-get -y purge gcc \
  && apt-get -y purge python \
  && apt-get -y purge ncurses-bin --allow-remove-essential \
  && apt-get -y purge grub-common --allow-remove-essential \
  && apt-get -y purge ncurses-term --allow-remove-essential \
  && apt-get -y purge manpages-dev \
  # && apt-get -y purge grub-pc-bin --allow-remove-essential \
  && apt-get -y autoremove \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* \
  /tmp/* \
  /var/tmp/*
WORKDIR /root
RUN mkdir /var/run/sshd \
  && echo 'root:default' | chpasswd \
  && sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config \
  && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd \
  && echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22
EXPOSE 80
EXPOSE 8080
EXPOSE 8090
EXPOSE 9090
EXPOSE 1812/udp
EXPOSE 1813/udp
COPY nap-dos/flaskserver.py /root
COPY nap-dos/webserver.py /root
COPY nap-dos/entrypoint.sh /root
RUN chmod +x /root/entrypoint.sh
WORKDIR /root
CMD /root/entrypoint.sh && tail -f /dev/null
#CMD [ "python3", "webserver.py" ]
