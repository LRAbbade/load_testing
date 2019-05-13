FROM python:3.7

COPY . /home/locust
WORKDIR /home/locust

VOLUME .:/home/locust

RUN pip install -r requirements.txt

EXPOSE 5557 5558 8089

RUN chmod 755 start.sh

ENTRYPOINT [ "/home/locust/start.sh" ]
