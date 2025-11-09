FROM python:3.10
ENV PYTHONUNBUFFERED 1
ADD . /tmp
ARG passwd ${passwd}
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources
RUN apt update && apt install -y openssh-server sshpass git autossh python3-pip --fix-missing
RUN pip install -r /tmp/requirements.txt -i https://mirrors.ustc.edu.cn/pypi/web/simple
RUN echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
RUN echo root:${passwd} | chpasswd
RUN cp /tmp/config /root/.ssh/ && ssh-keygen -t rsa -P '' -f /root/.ssh/id_rsa \
&& sshpass -p ${passwd} ssh-copy-id -o "StrictHostKeyChecking no" -i "/root/.ssh/id_rsa.pub" jump
RUN mkdir /src
WORKDIR /src
