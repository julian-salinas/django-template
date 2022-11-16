# django-template

This template counts with:
- Docker
- Django custom settings for:
  - Postgres database
  - Middleware
  - Third Party Apps
  - Swagger
  - Redoc
  - Logging
  - **REST Framework** 
- Django database adminer

For start using it, setup the docker containers:
```bash
docker-compose up
```

Enter the Django app contanier
```bash
docker exec -it app bash
```

Make the migrations. You can find all the Django commands in [this document](/docs/django-commands.md), and the Docker commands you'll probably need in
[this document](/docs/docker-cheatsheet.md)