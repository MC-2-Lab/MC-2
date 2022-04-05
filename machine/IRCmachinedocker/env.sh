#!/usr/bin/env bash

export user=$1;
export passwd=$2;

# 默认文件夹名
project_path=$(pwd);
project_name="${project_path##*/}";
export COMPOSE_PROJECT_NAME=$project_name;

alias build="docker-compose build"

alias start="docker-compose up -d"
alias debug="docker-compose up"

alias site="docker-compose run --rm --service-port machinenginx bash"
