FROM python:3

# Add user
RUN useradd -ms /bin/bash gandhi

# Install python packages
COPY requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip3 install -r requirements.txt

#RUN pip install -r requirements.txt
CMD chmod +x /home/gandhi/workspace/hirearefugee/docker/india/init.sh
ENTRYPOINT ["/home/gandhi/workspace/hirearefugee/docker/india/init.sh"]