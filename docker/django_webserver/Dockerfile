FROM python:3

# Add user
RUN useradd -ms /bin/bash gandhi

# Install python packages
COPY requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip3 install -r requirements.txt

#RUN pip install -r requirements.txt
CMD chmod +x /media/docker/workspace/hirearefugee/docker/django_webserver/init.sh
ENTRYPOINT ["/media/docker/workspace/hirearefugee/docker/django_webserver/init.sh"]