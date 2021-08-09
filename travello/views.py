from travello.models import Destination
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

def index(request):
     dests=Destination.objects.all()
    
     return render(request,"index.html",{'dests':dests})