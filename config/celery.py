import os

from celery import Celery

os.environ.setdefault(key="DJANGO_SETTINGS_MODULE", value="config.settings")

celery_app: Celery = Celery(main="config")

celery_app.config_from_object(obj="django.conf:settings", namespace="CELERY")

celery_app.autodiscover_tasks()

celery_app.conf.broker_connection_retry_on_startup = True
