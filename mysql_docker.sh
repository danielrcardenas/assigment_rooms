#!/usr/bin/env bash
mkdir -p /storage/docker/mysql-datadir
chown -R admin.innova:admin.innova /var/storage/docker/
chcon -Rt svirt_sandbox_file_t /var/storage/docker/mysql-datadir/ # For RedHat based OS


docker run -ti --detach --user 1001 --name=innova-mysql --env="MYSQL_ROOT_PASSWORD=root.2017" \
 --publish 6603:3306 --volume=/home/admin.innova/docker/innova-mysql/conf.d:/etc/mysql/conf.d:Z \
 --volume=/var/storage/docker/mysql-datadir:/var/lib/mysql:Z \
  -v /etc/group:/etc/group:ro -v /etc/passwd:/etc/passwd:ro \
   mysql:8.0

docker exec -i -t innova-mysql /bin/bash

#https://severalnines.com/blog/mysql-docker-containers-understanding-basics