from django.http import HttpResponse
from django.shortcuts import render

def text_response(request):
    return HttpResponse("Hello, this is a text response!")

def html_response(request):
    return render(request, 'myapp/template.html')
