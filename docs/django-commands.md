# django-commands

## **Database related commands**
1. Make migrations
```bash
python manage.py makemigrations
```

2. Migrate
```bash
python manage.py migrate
```

3. Shell for running queries
```bash
python manage.py shell
```

## **Create projects/apps**
### Start a new project
```bash
django-admin startproject <project-name>
```

### Start a new app
```bash
python manage.py startapp mi_app
```

## **Users**
### Create superuser
```bash
python manage.py createsuperuser
```

## **Run server**
```bash
python manage.py runserver <ip>:<port>
```

## **Collect static files**
```bash
python manage.py collectstatic --noinput
```