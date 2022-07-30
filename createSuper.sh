#!/bin/bash -x

python manage.py migrate --noinput || exit 1
python manage.py createSuper || exit 1
exec "$@"

