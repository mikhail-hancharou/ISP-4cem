from django.http import HttpResponse
from django.shortcuts import render


def blog(request):
    return HttpResponse("<h1>OMG THAT IS BLOG</h1>")
