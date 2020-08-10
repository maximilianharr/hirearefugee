# Hire A Refugee
We are a group of volunteers that desire to provide a platform / network for refugees to find a job and get in contact with their local community.  
Follow us on [Instagram](https://www.instagram.com/hirearefugee/) or join our [Github project](https://github.com/maximilianharr/hirearefugee)!  

## Overview
This is a django webserver which provides a platform to help refugees to get a job and in contact with their local community.  

## Getting Started

### Installation
```bash
mkdir -p ${HOME}/workspace
cd ${HOME}/workspace
git clone https://github.com/maximilianharr/hirearefugee.git hirearefugee
python3 -m venv venv_hirearefugee
source ${HOME}/workspace/venv_hirearefugee/bin/activate
python3 -m pip install django
```

### Start Django Server Locally
```bash
source ${HOME}/workspace/venv_hirearefugee/bin/activate
python3 manage.py runserver
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

## License

[Apache License 2.0](LICENSE)
