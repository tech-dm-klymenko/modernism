#!/bin/bash

set -Eeuxo pipefail

python manage.py migrate
python manage.py collectstatic --noinput

exec "$@"