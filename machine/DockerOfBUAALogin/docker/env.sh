#!/usr/bin/env bash

export user=$1;
export pwd=$2;

alias build="docker-compose build"
# TODO: 使用脚本，包括初次使用，退出-继续运行/停止，重入等
alias start="docker-compose up -d"
alias debug="docker-compose up"

# alias site="docker-compose run --service-port ldl bash"
