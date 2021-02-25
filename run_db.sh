#!/usr/bin/bash -x
#docker pull mysql:8.0.23
#docker pull python:latest

# Check if server is already up, and start it if needed.
DBSERVER_ID=`docker ps | grep dbserver | cut -f1 -d" "`
if [ -z "${DBSERVER_ID}" ]; then
  echo "DB SERVER IS DOWN: STARTING UP"
  docker rm dbserver
  docker run --name dbserver -e MYSQL_ROOT_PASSWORD=123 -e MYSQL_DATABASE=DB_LEARNING -e MYSQL_USER=jojo -e MYSQL_PASSWORD=3892688 -d mysql:8.0.23
  sleep 30
fi
DBSERVER_ID=`docker ps | grep dbserver | cut -f1 -d" "`
echo "Db server started with id ${DBSERVER_ID}"

#docker logs -f "$DBSERVER_ID" 2>&1 | grep -q "/usr/sbin/mysqld: ready for connections. Version: '8.0.23'  socket: '/var/run/mysqld/mysqld.sock'  port: 3306"

#docker build -t jojo .
#docker run --link dbserver -e MYSQL_USER=testpy -e MYSQL_PASS=testpypassword -e MYSQL_DATABASE=testpy -e MYSQL_HOST=dbserver jojo
#read $hola
