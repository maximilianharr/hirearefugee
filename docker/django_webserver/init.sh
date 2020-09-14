#!/bin/bash
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Greetings
printf "${NC}--------------------------------------------------${NC}\n"
printf "${GREEN}Hello $(whoami)! Welcome to $(hostname -s)!${NC}\n"
printf "${NC}--------------------------------------------------${NC}\n"

# Init
WEBSERVER_DIR=/media/docker/workspace/hirearefugee

# Run Webserver

if [ ${USE_GUNICORN_NGINX} == "true" ]; then

    cd ${WEBSERVER_DIR}/docker/django_webserver/bin
    ./gunicorn_start
else
    python3 ${WEBSERVER_DIR}/hirearefugee/manage.py runserver 0.0.0.0:8000
fi
