#!/usr/bin/env bash

export user=$1;
export passwd=$2;


alias build="docker-compose build"

alias start="docker-compose up -d"
alias debug="docker-compose up"

alias site="docker-compose run --rm --service-port machinenginx bash"
