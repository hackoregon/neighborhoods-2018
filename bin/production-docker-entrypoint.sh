#! /bin/bash

# http://linuxcommand.org/lc3_man_pages/seth.html:
# -e  Exit immediately if a command exits with a non-zero status.
set -e

echo Debug: $DEBUG

python -Wall manage.py collectstatic --noinput

gunicorn $PROJECT_NAME.wsgi -c gunicorn_config.py
