from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    response_text = "You're at Ajit's helloworld page.<br> Trying Django for 1st time. \
                    <br> Just trying random text here."
    return HttpResponse(response_text)
