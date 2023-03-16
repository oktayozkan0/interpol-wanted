FROM ubuntu:focal


RUN apt-get update
RUN apt-get install -y python3.8 python3-pip
RUN python3 -m pip install --upgrade pip
RUN apt-get clean
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME
COPY . $APP_HOME/
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]