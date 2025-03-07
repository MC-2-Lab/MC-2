#!/usr/bin/env bash
apt-get clean
sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
apt-get update --fix-missing
apt-get install -y python3 python3-pip nginx ssh sshpass
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

pip3 install psutil -i https://pypi.tuna.tsinghua.edu.cn/simple
pip3 install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


# export PATH = xx
