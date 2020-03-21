# Develop

check:
	black --check .
	isort --check-only --recursive
	flake8
	mypy .

checkcommit:
	black .
	isort --recursive
	flake8
	mypy .

collectstatic:
	python manage.py collectstatic --clear --noinput

dev:
	pip install -q -U pip~=20.0.2 pip-tools~=4.5.0
	pip-sync requirements/dev.txt

migrate:
	python manage.py migrate --noinput

migrations:
	python manage.py makemigrations --no-header

pip:
	pip install -q -U pip~=20.0.2 pip-tools~=4.5.0
	pip-compile $(p) -q -U -o requirements/common.txt requirements/common.ini
	pip-compile $(p) -q -U -o requirements/dev.txt requirements/dev.ini
	pip-compile $(p) -q -U -o requirements/prod.txt requirements/prod.ini
	pip-compile $(p) -q -U -o requirements/tests.txt requirements/tests.ini
	pip-compile $(p) -q -U -o requirements/local.txt requirements/local.ini

test:
	tox -e coverage,reporthtml,report

# Ansible

alpha:
	cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml --skip-tags "init,database,restore"

beta:
	cd deploy && TARGET=beta ansible-playbook -vv deploy.yml --skip-tags "init,database,restore"

initalpha:
	cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml --skip-tags "restore"

initbeta:
	cd deploy && TARGET=beta ansible-playbook -vv deploy.yml --skip-tags "restore"

initproduction:
	cd deploy && TARGET=production ansible-playbook -vv deploy.yml --skip-tags "restore"

production:
	cd deploy && TARGET=production ansible-playbook -vv deploy.yml --skip-tags "init,database,restore"

restorealpha:
	cd deploy && TARGET=alpha ansible-playbook -vv deploy.yml --skip-tags "init"

restorebeta:
	cd deploy && TARGET=beta ansible-playbook -vv deploy.yml --skip-tags "init"

restoreproduction:
	cd deploy && TARGET=production ansible-playbook -vv deploy.yml --skip-tags "init"
