#!/bin/bash

echo ${gitlabip}
sshpass -p ${passwd} ssh -o StrictHostKeyChecking=no -L 0.0.0.0:8081:${gitlabip}:8081 ywz@${openip} -p ${openport} &
sshpass -p ${passwd} ssh -o StrictHostKeyChecking=no -L 0.0.0.0:8022:${gitlabip}:8022 ywz@${openip} -p ${openport} &

python django1/manage.py runserver 0.0.0.0:8000 > docker/log/django.log 2>&1