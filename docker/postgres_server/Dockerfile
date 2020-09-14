FROM postgres:12

RUN apt-get update

# Install Postgis 
RUN apt-get install -y postgresql-12-postgis-3 
RUN apt-get install -y postgresql-12-postgis-3-scripts

# Install python 
# needed to update database if new files exist
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

# Install python packages
COPY requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip3 install -r requirements.txt