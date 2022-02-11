# pydantic_car
Exploratory demo of using pydantic with redis.


# Helpful redis commands for cli
 - `redis-cli` # opens the cli
 - `redis-cli ping` # should get PONG as a return, tells you that redis is running
 - `redis-server --daemonize yes` # starts server as background task
 - reset the redis db
   - `redis-cli FLUSHDB`
   - `redis-cli FLUSHALL`

## quickstart redis json server with docker
```docker run -p 6379:6379 --name redis-redisjson redislabs/rejson:latest```