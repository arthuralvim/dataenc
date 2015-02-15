# Makefile dataenc

DJADMIN_PY=$(VIRTUAL_ENV)/bin/django-admin.py
FABRIC=$(VIRTUAL_ENV)/bin/fab
GUNICORN=$(VIRTUAL_ENV)/bin/gunicorn
MANAGE_PY=$(VIRTUAL_ENV)/bin/python manage.py
PIP=$(VIRTUAL_ENV)/bin/pip
PROVY=$(VIRTUAL_ENV)/bin/provy
PY=$(VIRTUAL_ENV)/bin/python
UWSGI=$(VIRTUAL_ENV)/bin/uwsgi

SETTINGS_DEV=dataenc.settings.dev
SETTINGS_PROD=dataenc.settings.prod


# These targets are not files
.PHONY: all check.venv check.app check.file check.settings check.branch check.user check.email dev prod requirements shell clean runserver db.delete.sqlite3 migrate db.reset static heroku.create heroku.remote heroku.db.reset heroku.static heroku.migrate open

all: help

help:
	@echo 'Just a makefile to help django projects.'

check.venv:
	@if test "$(VIRTUAL_ENV)" = "" ; then echo "VIRTUAL_ENV is undefined"; exit 1; fi

check.app:
	@if test "$(APP)" = "" ; then echo "APP is undefined"; exit 1; fi

check.file:
	@if test "$(FILE)" = "" ; then echo "FILE is undefined"; exit 1; fi

check.settings:
	@if test "$(SETTINGS)" = "" ; then echo "SETTINGS is undefined"; exit 1; fi

check.branch:
	@if test "$(BRANCH)" = "" ; then echo "BRANCH is undefined"; exit 1; fi

check.user:
	@if test "$(USER)" = "" ; then echo "USER is undefined"; exit 1; fi

check.email:
	@if test "$(EMAIL)" = "" ; then echo "EMAIL is undefined"; exit 1; fi

# SETTINGS FILES

dev: check.venv
	$(eval SETTINGS:=$(SETTINGS_DEV))

prod: check.venv
	$(eval SETTINGS:=$(SETTINGS_PROD))

# ---

# UTIL

requirements:
	@$(PIP) install -r requirements.txt

shell: check.settings
	@$(MANAGE_PY) shell --settings=$(SETTINGS)

clean:
	@find . -name '*.pyc' -exec rm -f {} \;
	@find . -name 'Thumbs.db' -exec rm -f {} \;
	@find . -name '*~' -exec rm -f {} \;

# ---

# SERVER

runserver: check.settings
	@$(MANAGE_PY) runserver --settings=$(SETTINGS)

# ---

# DATABASE

db.delete.sqlite3:
	@rm dataenc/db/dataenc.sqlite3

migrate: check.settings
	@$(MANAGE_PY) migrate --settings=$(SETTINGS)

db.reset: db.delete.sqlite3 migrate

# STATIC

static: check.settings
	@$(MANAGE_PY) collectstatic --clear --noinput --settings=$(SETTINGS)

# ---

#  HEROKU

heroku.create:
	@heroku create --stack cedar dataenc

heroku.remote:
	@heroku git:remote -a dataenc
	# git remote add heroku git@heroku.com:dataenc.git

heroku.db.reset:
	@heroku heroku pg:reset DATABASE_URL

heroku.static:
	@heroku run python manage.py collectstatic --clear --noinput --settings=$(SETTINGS_PROD)

heroku.migrate:
	@heroku run python manage.py migrate --settings=$(SETTINGS_PROD)

open:
	@heroku open

# ---
