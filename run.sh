#!/bin/bash

# Activate the virtual environment
source /home/projects/django/DialogNetz/backend/dia_env/bin/activate

# Install the requirements from the requirements.txt file
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

# Run the Django development server
python manage.py runserver 8005
