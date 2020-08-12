# Docker (Docker Inc.)
A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings. [1]

[1] https://www.docker.com/resources/what-container

# Docker Containers
Each main docker has a separate folder with detailed documentation (README.md).

## Docker Cheatsheat

### Show all containers
```bash
docker ps -a
```

### Remove all containers
```bash
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
```

## Naming conventions
We honor great role model by naming our containers after them.

### Containers / Computers
Country (e.g. India)

### Users
Role model (e.g. Ghandi)

