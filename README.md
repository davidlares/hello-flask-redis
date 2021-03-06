# Hello Flask w/ Docker

A simple web Based project with Python Flask handled by Docker and CircleCI.

## Files

1. The `app.py` (inside the `app` directory) is a simple development hello world Flask Script that hosts the remote access from clients and other containers

2. The `Dockerfile` with deployment instructions.

## Build

Run: `docker build -t app:v0.1 .`

## Test and Run

Please run: `docker run -d -p 5000:5000 [ID of the image]`

Notice that Flask runs on 5000 by default -> same port forwarding, using the -d (daemon)

First, we need to check where is the python server running (IP), for linux: localhost and for win/mac: docker VM

Check IP: `docker-machine ls` get the IP and paste it on the browser

## Run commands

Run commands with exec: run commands on a container

`docker exec -it [container ID] bash`, this will enter into a bash session

You can also check user and directory with: `whoami` and `pwd`, or `cd /home/admin` or display running processes: `ps aux`


## Using Redis for a microservice approach

Redis is an In-memory data structure store, used as database, cache and message broker. It uses a built-in replication and different levels of on-disk persistence.

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
