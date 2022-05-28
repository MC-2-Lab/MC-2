#!/bin/bash

echo ${gitlabip}
sshpass -p ${passwd} ssh -L 8081:${gitlabip}:8081 ywz@${openip} -p ${openport} &
sshpass -p ${passwd} ssh -L 8022:${gitlabip}:8022 ywz@${openip} -p ${openport} &
