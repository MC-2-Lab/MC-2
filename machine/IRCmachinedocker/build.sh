#!/usr/bin/env bash
apt-get clean

apt-get update --fix-missing
apt-get install -y python3 python3-pip nginx ssh sshpass
# systemctl enable nginx.service

pip3 install psutil
pip3 install -r /tmp/requirements.txt


# export PATH = xx