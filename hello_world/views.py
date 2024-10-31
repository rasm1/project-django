from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    if request.method == "POST":
        return HttpResponse("you must have posted something")
    elif request.method == "GET":
        return HttpResponse(request.method)