# {{cookiecutter.project_name}} <!-- omit in toc -->

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

A [Django](https://docs.djangoproject.com) project using [uWSGI](https://uwsgi-docs.readthedocs.io) as application server.

## Index <!-- omit in toc -->

- [Conventions](#conventions)
- [Initialization](#initialization)
  - [Virtual environment](#virtual-environment)
  - [Requirements](#requirements)
- [Git](#git)
    - [Git initialization](#git-initialization)
    - [Git clone](#git-clone)
    - [Git hooks](#git-hooks)
- [Quickstart](#quickstart)
- [Libraries](#libraries)
  - [List outdated libraries](#list-outdated-libraries)
  - [Update libraries](#update-libraries)
  - [Install libraries](#install-libraries)
- [Testing](#testing)
- [Static files](#static-files)
- [Continuous Integration](#continuous-integration)
  - [Jenkins](#jenkins)
  - [Gitlab CI](#gitlab-ci)
  - [Bitbucket pipelines](#bitbucket-pipelines)
- [Database](#database)
  - [Create](#create)
  - [Drop](#drop)
  - [Reset](#reset)
  - [Dump](#dump)
- [Deploy](#deploy)
  - [Initialize](#initialize)
  - [Deploy](#deploy-1)
  - [Restore](#restore)

## Conventions

- replace `projects` with your actual projects directory
- replace `git_repository_url` with your actual git repository url

## Initialization

We suggest updating pip to the latest version and using a virtual environment to wrap all your libraries.

### Virtual environment

**IMPORTANT**: Please, create an empty virtual environment, with the right python version, and activate it.
To install and use virtualenv, please, visit the official [Python tutorial](https://docs.python.org/3/tutorial/venv.html)

### Requirements

[Invoke](https://www.pyinvoke.org/) must be installed before initializing the project.

```shell
({{cookiecutter.project_slug}}) $ pip install -U invoke
```

## Git

#### Git initialization

In order to initialize git and sync the project with an existing repository:

```shell
({{cookiecutter.project_slug}}) $ cd ~/projects/{{cookiecutter.project_slug}}
({{cookiecutter.project_slug}}) $ inv gitinit git_repository_url
```

#### Git clone

To get the existing project, change directory, clone the project repository and enter the newly created **{{cookiecutter.project_slug}}** directory:

```shell
({{cookiecutter.project_slug}}) $ cd ~/projects/
({{cookiecutter.project_slug}}) $ git clone GIT_REPOSITORY_URL {{cookiecutter.project_slug}}
({{cookiecutter.project_slug}}) $ cd {{cookiecutter.project_slug}}
```

**NOTE** : Make sure you switch to the correct branch (e.g. `git checkout develop`)

#### Git hooks

To install pre-commit into your git hooks run the below command. pre-commit will now run on every commit. Every time you clone a project using pre-commit running pre-commit install should always be the first thing you do.

```shell
({{cookiecutter.project_slug}}) $ pre-commit install
```

## Quickstart

Invoke init and follow instructions, to configure the project:

```shell
({{cookiecutter.project_slug}}) $ inv init
```

## Libraries

### List outdated libraries

To list all outdated installed libraries:

```shell
({{cookiecutter.project_slug}}) $ pip list -o
```

### Update libraries

Edit the appropriate .ini requirements file, to add/remove pinned libraries or modify their versions.

To update the compiled requirements files (`requirements/*.txt`), execute:

```shell
({{cookiecutter.project_slug}}) $ make pip
```

Alternatively, in order to update specific dependent libraries to the latest version (e.g. urllib3), execute:
￼
```shell
({{cookiecutter.project_slug}}) $ make pip p='-P urllib3'
```

### Install libraries

To install the just updated requirements (e.g. `requirements/dev.txt`), execute:

```shell
({{cookiecutter.project_slug}}) $ make dev
```

## Testing

To run the full test suite, with coverage calculation, execute:

```shell
({{cookiecutter.project_slug}}) $ make test
```

## Static files

To collect static files, execute:

```shell
({{cookiecutter.project_slug}}) $ make collectstatic
```

## Continuous Integration

Depending on the CI tool, you might need to configure Django environment variables.

### Jenkins

Use the following command as a shortcut to configure the continuous integration.

```shell
pip install tox
export DATABASE_URL=postgres://postgres:postgres@localhost:5432/{{cookiecutter.project_slug}}
export DJANGO_SECRET_KEY=<django_secret_key>
tox -e coverage,reportxml
```

### Gitlab CI

The configuration file `.gitlab-ci.yml` should work as is, needing no further customization.

### Bitbucket pipelines

The configuration file `bitbucket-pipelines.yml` should work as is, needing no further customization.

## Database

### Create

To create a local database (database settings from `.env`):

```shell
({{cookiecutter.project_slug}}) $ inv createdb
```

### Drop

To drop the local database (database settings from `.env`):

```shell
({{cookiecutter.project_slug}}) $ inv dropdb
```

### Reset

To reset database execute (database settings from `.env`):

```shell
({{cookiecutter.project_slug}}) $ inv dropdb
({{cookiecutter.project_slug}}) $ inv createdb
```

**NOTE**: Beware all data will be lost.

### Dump

To dump the local database into `deploy/dump.sql.bz2` (database settings from `.env`):

```shell
({{cookiecutter.project_slug}}) $ inv dumpdb
```

## Deploy

The project is partially configured to use Ansible to deploy the project. For each instance to deploy (e.g. "alpha"), there must be a config file (e.g. `deploy/alpha.yml`) and an item in the hosts file.

Use provided `deploy/alpha.yml.tpl` and `deploy/hosts.tpl` as templates for, respectively, the configuration and the hosts files. Rename them removing the `.tpl` suffix. The obtained files will not be versioned.

This project contains makefile commands for "alpha". If needed, duplicate those and use them as templates for additional instances (e.g. "beta" or "prod").

Both the remote server and the continuous integration system need `node.js`, in order to automatically build static files. If such module bundler is not necessary, remove unused commands from the Makefile `ci` command and from `deploy/deploy.yml`.

### Initialize

Each instance (e.g. "alpha") should be initialized, executing only **once**:

```shell
({{cookiecutter.project_slug}}) $ make initalpha
```

### Deploy

To deploy a specific instance (e.g. "alpha"), execute:

```shell
({{cookiecutter.project_slug}}) $ make alpha
```

### Restore

To restore a local database dump (`deploy/dump.sql.bz2`) and deploy a specific instance (e.g. "alpha"), execute:

```shell
({{cookiecutter.project_slug}}) $ make restorealpha
```
