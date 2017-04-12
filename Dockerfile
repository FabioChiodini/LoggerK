FROM alpine
MAINTAINER fabio.chiodini@gmail.com

RUN apk --update add git python py-pip && rm -f /var/cache/apk/*
RUN pip install flask requests python-logstash
COPY Logger.py /tmp/
#EXPOSE 8080
ENTRYPOINT ["python","/tmp/LoggerK.py"]
