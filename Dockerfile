FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install python3-pip -y

COPY . /codeserver
WORKDIR /codeserver

RUN pip install -r requirements.txt

ENTRYPOINT [ "python3" ]
CMD ["app.py"]