from django.http import HttpResponse
from . import tasks

# Create your views here.


def home(request):
    """
    The home function is responsible for uploading a dog image to the server.
    It does this by calling the download_dog task, which downloads a random dog image from 
    the internet and saves it in /tmp/dog.jpg on the server.

    """
    tasks.download_dog.delay()
    return HttpResponse('<h1>Uploading a dog image...</h1>')
