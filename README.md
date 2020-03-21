# Django uWSGI Cookiecutter <!-- omit in toc -->

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

A [Django](https://docs.djangoproject.com) project cookiecutter using [uWSGI](https://uwsgi-docs.readthedocs.io) as application server.

## Index <!-- omit in toc -->

- [Conventions](#conventions)
- [Requirements](#requirements)
- [Quickstart](#quickstart)

## Conventions

In the following instructions:

- replace `projects` with your actual projects directory
- replace `My project name` with your chosen project name

## Requirements

[Cookiecutter](https://cookiecutter.readthedocs.io) must be installed before initializing the project.

```shell
$ pip install --user cookiecutter
```

## Quickstart

Change directory and create a new project as in this example:

```shell
$ cd ~/projects/
$ cookiecutter https://github.com/20tab/django-uwsgi-cookiecutter
project_name: My project name
project_slug [myprojectname]:
domain_url [myprojectname.com]:
$ cd myprojectname
```
