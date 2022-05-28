#!/bin/bash

nohup sshpass -p ${passwd} ssh -o StrictHostKeyChecking=no -L 0.0.0.0:8081:${gitlabip}:8081 ywz@${openip} -p ${openport} &
nohup sshpass -p ${passwd} ssh -o StrictHostKeyChecking=no -L 0.0.0.0:8022:${gitlabip}:8022 ywz@${openip} -p ${openport} &

