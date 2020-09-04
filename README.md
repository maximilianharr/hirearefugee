# Hire A Refugee

## Overview
We are a group of volunteers that desire to provide a platform / network for refugees to find a job and get in contact with their local community.  
Follow us on [Instagram](https://www.instagram.com/hirearefugee/) or join our [Github project](https://github.com/maximilianharr/hirearefugee)!  

## Getting Started

### Prerequisites
Our webserver is completely containerized. Thus, you can run it in any OS (preferebly Ubuntu 18.04 / 20.04) without installing any additional software :) ... except for docker and docker-compose. 
If you run on Ubuntu you can use [this script](https://github.com/maximilianharr/code_snippets/blob/master/sh/install_docker.sh) to install docker and docker-compose.

You can check if you have docker and docker-compose already installed via:
```bash
docker --version
docker-compose --version
```

Check if docker is working:
```bash
docker run hello-world
```

### Installation
Clone repository
```bash
mkdir -p ${HOME}/workspace
cd ${HOME}/workspace
git clone https://github.com/maximilianharr/hirearefugee.git hirearefugee
```

#### Build/pull Docker Images and Run The Webserver
Build docker container and run
```bash
cd ${HOME}/workspace/hirearefugee/docker/all
docker-compose build
docker-compose up
```

#### Create Database and Migrate
```bash
docker exec -it all_postgres_server_1 bash -c 'createdb -U postgres -h localhost -p 5432 hirearefugeedb'
docker exec -it all_django_webserver_1 bash -c 'python3 /media/docker/workspace/hirearefugee/hirearefugee/manage.py makemigrations'
docker exec -it all_django_webserver_1 bash -c 'python3 /media/docker/workspace/hirearefugee/hirearefugee/manage.py migrate'
```

#### Open Django in Browser
Open the webserver in Firefox
```bash
firefox http://localhost:8000/
```

## Debugging

### Open Bash in Running Container
Open bash in running docker container (e.g. to create new apps)
```bash
docker container ls
docker exec -it ${CONTAINER_ID} /bin/bash
```

### Open Bash in New Container
When you want to perform some shell operations inside a new docker docker container you need to overwrite the --entrypoint.
```bash
docker run --entrypoint "/bin/bash" -u ${USER} -it ${DOCKER_IMAGE}
```

## Issues

## Contribution

## License

## License

[Apache License 2.0](LICENSE)
