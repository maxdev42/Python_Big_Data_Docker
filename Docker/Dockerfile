FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt \
    apt-get install vim \
    apt-get install pip3 \
    apt get update

EXPOSE 8000

COPY . .

CMD [ "python", "./your-daemon-or-script.py" ]
