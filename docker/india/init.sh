#!/bin/bash
RED='\033[0;31m'
NC='\033[0m' # No Color

# Greetings
printf "${NC}--------------------------------------------------${NC}\n"
printf "${RED}Hello $(whoami)! Welcome to $(hostname -s)!${NC}\n"
printf "${NC}--------------------------------------------------${NC}\n"

# Commands
WEBSERVER_DIR=/home/$(whoami)/workspace/hirearefugee
source ${WEBSERVER_DIR}/setup.bash

printf "${RED} Success ${NC}\n"

python3 ${WEBSERVER_DIR}/hirearefugee/manage.py runserver 0.0.0.0:8000