# Hire A Refugee
We are a group of volunteers that desire to provide a platform / network for refugees to find a job and get in contact with their local community.  
Follow us on [Instagram](https://www.instagram.com/hirearefugee/) or join our [Github project](https://github.com/maximilianharr/hirearefugee)!  

## Overview
This is a django webserver which provides a platform to help refugees to get a job and in contact with their local community.  

## Getting Started

### Prerequisites
Our webserver is containerized. Thus, you can run it in any OS without installing any additional software :) ... except for docker and docker-compose. 
However, this installattion guide assumes you run in Ubuntu. If you're on Windows on MAC, you'll find the docker setup online.  

For details see the install.sh script in the docker folder. You can check if you have docker and docker-compose already installed via:
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

### Build/pull Docker Images and Run The Webserver
Build docker container and run
```bash
cd ${HOME}/workspace/hirearefugee/docker/india
docker-compose up
```

Open the webserver in Firefox
```bash
firefox http://localhost:8000/
```

### Working in The Current Container
Open bash in running docker container (e.g. to create new apps)
```bash
docker container ls
docker exec -it ${CONTAINER_ID} /bin/bash
```

### Working in New Container
When you want to perform some shell operations (e.g. python3 manage.py makemigations/migrate) inside your docker you can do so. 
As we typically use shell scripts as docker entrypoints (e.g. launch the webserver) you need to overwrite the --entrypoint.
```bash
docker run --entrypoint "/bin/bash" -u gandhi -h india -it hirearefugee/india
```

## Documentation

### Start New Project
```bash
django-admin startproject ${PROJECT_NAME}
```

### Add New App
```bash
python3 manage.py startapp ${APP_NAME}
```

### Migrate Server
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Create New SuperUser
```bash
python3 manage.py createsuperuser
```

## Issues

## Contribution

## License