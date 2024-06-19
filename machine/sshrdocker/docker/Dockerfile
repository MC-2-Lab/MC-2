FROM python:3.7
ENV PYTHONUNBUFFERED 1
ADD . /tmp
ARG passwd ${passwd}
# RUN pip install -r /tmp/requirements.txt
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources
RUN sh /tmp/build.sh
# RUN apt update && apt install -y openssh-server sshpass --fix-missing
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN echo root:${passwd} | chpasswd
RUN mkdir /root/.ssh && cp /tmp/config /root/.ssh/ && ssh-keygen -t rsa -P '' -f /root/.ssh/id_rsa \
&& sshpass -p ${passwd} ssh-copy-id -o "StrictHostKeyChecking no" -i "/root/.ssh/id_rsa.pub" txy
RUN mkdir /src
WORKDIR /src
