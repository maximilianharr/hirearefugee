# Hire A Refugee
We are a group of volunteers that desire to provide a platform / network for refugees to find a job and get in contact with their local community.  
Follow us on [Instagram](https://www.instagram.com/hirearefugee/) or join our [Github project](https://github.com/maximilianharr/hirearefugee)!  

## Overview
This is a django webserver which provides a platform to help refugees to get a job and in contact with their local community.  

## Getting Started With Docker (Recommended)

### Installation
Clone repository
```bash
mkdir -p ${HOME}/workspace
cd ${HOME}/workspace
git clone https://github.com/maximilianharr/hirearefugee.git hirearefugee
docker build -t ${HOME}/workspace/hirearefugee/docker/india india
```

### Start Django Server Locally
Build docker container and run
```bash
docker run --user gandhi --publish 8000:8000 --volume ${HOME}/workspace:/home/gandhi/workspace -h india -it hirearefugee/india bash
```

Open the webserver in Firefox
```bash
firefox http://localhost:8000/
```

### Working
Open bash in running docker container (e.g. to create new apps)
```bash
docker container ls
docker exec -it ${CONTAINER_ID} /bin/bash
```

## Getting Started Without Docker

### Installation
Django Installation
```bash
mkdir -p ${HOME}/workspace
cd ${HOME}/workspace
git clone https://github.com/maximilianharr/hirearefugee.git hirearefugee
sudo apt-get install python3-venv
python3 -m venv venv_hirearefugee
source ${HOME}/workspace/venv_hirearefugee/bin/activate
python3 -m pip install django
```

Adding psycopg2 for GeoDjango
```bash
sudo apt install libpq-dev
python3 -m pip install psycopg2
```

### Start Django Server Locally
```bash
source ${HOME}/workspace/venv_hirearefugee/bin/activate
python3 manage.py runserver
```

Open the webserver in Firefox  
```bash
firefox http://localhost:8000/
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