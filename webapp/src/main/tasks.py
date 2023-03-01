import requests as r
import uuid

from celery import shared_task
from django.conf import settings

# Create your tasks here

DOG_URL = 'https://placedog.net/1080/1080?random'


@shared_task
def download_dog():
    resp = r.get(DOG_URL)
    file_ext = resp.headers.get('Content-Type').split('/')[1]
    file_name = settings.BASE_DIR / 'dogs' / \
        (str(uuid.uuid4()) + "." + file_ext)

    with open(file_name, 'wb') as f:
        for chunk in resp.iter_content(chunk_size=128):
            f.write(chunk)

    return True
