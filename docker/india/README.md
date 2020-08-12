# Alderaan
This docker container runs the first webserver

## Build
```bash
cd ~/workspace/docker
docker build -t hirearefugee/india india
```

## Run
```bash
docker run --user gandhi --publish 8000:8000 --volume ${HOME}/workspace:/home/gandhi/workspace -h india -it hirearefugee/india bash
```