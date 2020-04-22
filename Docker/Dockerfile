FROM ubuntu:18.04

RUN apt-get update && \
    apt-get -y install curl && \
    apt-get install -qy python3 && \
    apt-get install -qy python3-pip && \
    apt-get install -qy vim && \
    apt-get install -y git

RUN apt-get -y install git

RUN git clone https://github.com/maxdev42/python-big-data.git

WORKDIR /Docker
ADD . /workspace
WORKDIR /workspace

RUN pip3 freeze > requirements.txt && \
    pip3 install -r requirements.txt && \
    pip3 install jupyter

EXPOSE 8000


CMD workspace --port 8000
