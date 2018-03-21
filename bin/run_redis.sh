docker rm -f $(docker ps -aq --filter="name=redis")
docker run -p 6379:6379 -h redis --restart=always --name redis -d redis
