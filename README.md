# Hire A Refugee
This is a django webserver intented to help refugees to get a job and in contact with their local community.

## Overview

## Getting Started

### Installation
```bash
mkdir -p ${HOME}/workspace
cd ${HOME}/workspace
git clone https://github.com/maximilianharr/hirearefugee.git hirearefugee
python3 -m pip venv venv_hirearefugee
source ${HOME}/workspace/venv_hirearefugee/bin/activate
python3 -m pip install django
```

### Start Django Server Locally
```bash
source ${HOME}/workspace/venv_hirearefugee/bin/activate
python3 manage.py runserver
firefox http://localhost:8000/
```

### Migrate Server
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Documentation

## Issues

## Contribution

## License