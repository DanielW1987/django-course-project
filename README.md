# Readme

## Install Django into virtual environment

```shell
# Set up virtual environment (directory can be freely selected)
python3 -m venv ~/venv/django

# Entering the environment
source ~/venv/django/bin/activate

# Install django
python3 -m pip install django
```

Verify installation with:

```shell
python3 -m django --version
```

## Create a project

```shell
python3 -m django startproject {{ project name }}
```

## Create an app (sub-project / module)

```shell
python3 manage.py startapp {{ name }}
```

## Start a development server

```shell
python3 manage.py runserver
```
