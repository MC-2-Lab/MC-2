#!/usr/bin/env bash
# #换源
# sed -i s@/archive.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
# sed -i s@/security.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
# apt clean
apt-get update -y
apt-get install -y sudo ssh git net-tools sshpass
apt-get install -y python3-pip

pip3 install -r /tmp/requirements.txt
