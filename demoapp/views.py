from django.shortcuts import render
from django.http import HttpResponse

def demo1(req):
    return HttpResponse('This demo page')
