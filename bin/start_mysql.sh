docker rm -f $(docker ps -aq --filter="name=mysql")
docker run -p 3307:3306 -h mysql --restart=always --name mysql -e MYSQL_ROOT_PASSWORD=root -d mysql:latest
