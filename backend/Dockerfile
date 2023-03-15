FROM python:3.8

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV APP_HOME /usr/src/app

WORKDIR /$APP_HOME
COPY ./app $APP_HOME/
RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]