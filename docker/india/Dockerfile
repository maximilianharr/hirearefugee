FROM python:3

# Add user
RUN useradd -ms /bin/bash gandhi

# Configure Django
RUN python3 -m pip install django
RUN python3 -m pip install pillow
# Django chat
RUN python3 -m pip install channels
RUN python3 -m pip install channels_redis

#RUN pip install -r requirements.txt
CMD chmod +x /home/gandhi/workspace/hirearefugee/docker/india/init.sh
ENTRYPOINT ["/home/gandhi/workspace/hirearefugee/docker/india/init.sh"]