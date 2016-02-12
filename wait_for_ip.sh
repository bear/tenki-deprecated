#!/bin/bash

unamestr=`uname -s`
if [[ "$unamestr" == 'Darwin' ]]; then
  _IP=`docker-machine ip`
  WEB_IP="${_IP}"
  DRIVER_IP="${_IP}"
else
  WEB_IP=`docker inspect --format '{{ .NetworkSettings.IPAddress }}' tenki_web_1`
  DRIVER_IP=`docker inspect --format '{{ .NetworkSettings.IPAddress }}' tenki_chromedriver_1`
fi

for i in {1..5}; do
  curl -s "http://${WEB_IP}:8000" -o /dev/null && curl -s "http://${DRIVER_IP}:4444" -o  /dev/null && break;
  sleep 5
done

echo ${DRIVER_IP}
