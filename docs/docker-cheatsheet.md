# docker-cheatsheet

## Setup the containers
```bash
docker-compose up
```

## Stop the containers
You can force it doing `Ctrl + C`, but remember to:
```bash
docker-compose down
```

## Stop all containers (including the background running ones)
```bash
docker rm $(docker ps -a -f status=exited -f status=created -q)
```

## Run bash in the container
```bash
docker exec -it <container-name> bash
```

## Delete all containers
```bash
docker rm -f $(docker ps -qa)
```

## Delete all images
```bash
docker rmi -f $(docker images -aq)
```