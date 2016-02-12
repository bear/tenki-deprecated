#!/bin/sh

unamestr=`uname -s`
if [ "$unamestr" == 'Darwin' ]; then
  _IP=`docker-machine ip`
  export WEB_IP="${_IP}"
  export DRIVER_IP="${_IP}"
else
  export WEB_IP=`docker inspect --format '{{ .NetworkSettings.IPAddress }}' tenki_web_1`
  export DRIVER_IP=`docker inspect --format '{{ .NetworkSettings.IPAddress }}' tenki_chromedriver_1`
fi

for i in {1..5}; do
  curl -s "http://${WEB_IP}:8000" -o /dev/null && curl -s "http://${DRIVER_IP}:4444" -o  /dev/null && break;
  sleep 5
done
