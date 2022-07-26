#!/usr/bin/env bash
# #换源
# sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
# sed -i s@/security.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
# apt clean
apt-get update -y
apt-get install -y sudo ssh git net-tools sshpass --fix-missing
apt-get install -y openssh-server --fix-missing
apt-get install -y autossh --fix-missing
apt-get install -y python3-pip --fix-missing

pip3 install -r /tmp/requirements.txt
