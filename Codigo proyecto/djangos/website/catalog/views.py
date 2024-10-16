from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import doorRelease
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms
from .camera import *
from .apertura import *
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
import json


@gzip.gzip_page
def livefe(request):
    try:
        cam=VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass

def apertura(request):
    if request.method=='POST':
        apertura.abrir()
        response_data='successful'
        return JsonResponse(response_data)
    else:
        return HttpResponse(json.dumps({"nothing to see": "this is not happening"}), content_type="application/json")

def index(request,*args,**kwargs):
    datalist = doorRelease.objects.all()
    return render(request,'index.html',context= {'datalist':datalist})
