from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from decouple import config

# set the default Django settings module for the 'celery' program.
from asplinks import settings

from datetime import timedelta, datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asplinks.settings')

app = Celery('asplinks', broker=config('BROKER'))

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
from celery.task import task
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    result_backend='django-db',
)
app.conf.beat_schedule = {
    'events': {
        'task': 'download_files_scheduler',
        'schedule': timedelta(seconds=3600),
    },
}

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))


@task(name="download_files_scheduler")
def download_files():
    from main.views import download_latest
    from main.models import RemoteServers,LatestFiles
    current_date = datetime.now()
    if current_date.weekday() == 3:
        for ftp_obj in RemoteServers.objects.all():
            if LatestFiles.objects.filter(ftp_obj=ftp_obj):
                latestfile_obj = LatestFiles.objects.get(ftp_obj=ftp_obj)
                initial = False
                latest = latestfile_obj.latest
            else:
                initial = True
                latest = 0
            print(">>>>ftp_obj     ",ftp_obj.hostname)
            download_latest(ftp_obj.hostname, ftp_obj.user, ftp_obj.password, ftp_obj.countrycode, target_path=None,
                            initial=initial, latest=latest, ftp_obj=ftp_obj)
