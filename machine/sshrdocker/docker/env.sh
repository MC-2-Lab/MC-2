#!/usr/bin/env bash

export passwd=$1;
export user=$2
export pwd=$3

alias build="docker-compose build --build-arg passwd=$passwd"
# TODO: 使用脚本，包括初次使用，退出-继续运行/停止，重入等
alias start="docker-compose up -d"
alias debug="docker-compose up"

alias site="docker-compose run --service-port sshr"
