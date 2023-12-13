FROM python:3.12

LABEL maintainer="adnan.a@killadesign.com"

WORKDIR /beam-scheduler-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./SRC ./SRC

COPY ./assets ./assets

CMD ["python", "./SRC/main.py"]