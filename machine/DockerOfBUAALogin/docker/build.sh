#!/usr/bin/env bash
# #换源
sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list.d/debian.sources
# sed -i s@/security.ubuntu.com/@/mirrors.aliyun.com/@g /etc/apt/sources.list
# apt clean
apt-get update -y
apt-get install -y sudo net-tools
apt-get install -y python3-pip

pip3 install -r /tmp/requirements.txt -i https://mirrors.ustc.edu.cn/pypi/web/simple
