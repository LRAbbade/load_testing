FROM python:3.7

WORKDIR /home

RUN git clone https://github.com/LRAbbade/load_testing.git

WORKDIR /home/load_testing

RUN pip install -r requirements.txt

EXPOSE 5557 5558 8089

RUN chmod 755 start.sh

ENTRYPOINT [ "/home/load_testing/start.sh" ]
