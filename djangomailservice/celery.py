import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangomailservice.settings')

app = Celery('djangomailservice')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.

# load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.enable_utc = False

@app.task
def add(x, y):
    return x / y