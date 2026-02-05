import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

app = Celery("project")

app.config_from_object("django.conf:settings", namespace="CELERY")

# 🔑 THIS LINE IS CRITICAL
app.autodiscover_tasks()

