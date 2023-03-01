from django.http import HttpResponse

# Create your views here.


def home(request):
    # start a task
    return HttpResponse('<h1>Uploading a dog image...</h1>')
