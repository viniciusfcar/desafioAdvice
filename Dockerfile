FROM python:3
RUN apt-get update
RUN apt-get install -y cron vim
RUN apt-get install -y python3-dev default-libmysqlclient-dev
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN chmod +x ./createSuper.sh
ENTRYPOINT ["./createSuper.sh"]
