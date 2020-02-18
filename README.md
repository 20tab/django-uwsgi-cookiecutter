# Django uWSGI Cookiecutter

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

A [Django](https://docs.djangoproject.com) project cookiecutter using [uWSGI](https://uwsgi-docs.readthedocs.io) as application server.

> **NOTE**: for OSX check [uwsgi-emperor-mode](https://github.com/20tab/uwsgi-emperor-mode) to configure your own local server with emperor.

## Documentation <!-- omit in toc -->

- [Django uWSGI Cookiecutter](#django-uwsgi-cookiecutter)
  - [Conventions](#conventions)
  - [Workspace initialization](#workspace-initialization)
    - [Basic requirements](#basic-requirements)
  - [Setup a new project](#setup-a-new-project)
    - [Start Project](#start-project)
    - [Git initialization](#git-initialization)

## Conventions

In the following instructions:

- replace `projects` with your actual projects directory
- replace `project_name` with your chosen project name
- replace `git_repository_url` with your actual git repository url

## Workspace initialization

### Basic requirements

**Cookiecutter** must be installed before initializing the project.

```shell
$ pip install --user cookiecutter
```

## Setup a new project

This section explains the first steps when you need to create a new project.

### Start Project

Change directory and start a new project with this template:

```shell
$ cd ~/projects/
$ cookiecutter https://github.com/20tab/django-uwsgi-cookiecutter
project_name [django uwsgi cookiecutter]: project_name
project_slug [project_name]:
$ cd project_slug
```

### Git initialization

In order to initialize git and sync the project with an existing repository:

```shell
$ cd ~/projects/project_slug
$ inv gitinit GIT_REPOSITORY_URL
```
