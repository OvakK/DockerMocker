# Docker file to build Docker image of Flask app.


FROM ubuntu

RUN  apt update &&\
    apt install python3 -y &&\
    apt install python3-pip  -y &&\
    pip3 install flask

COPY . .

CMD ["python3", "hello.py"]

