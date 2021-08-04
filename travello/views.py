from travello.models import Destination
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

def index(request):
     dest1=Destination()
     dest1.name="Mumbai"
     dest1.img='services1.jpg'
     dest1.desc="The city never sleeps"
     dest1.price=7000
     dest1.offer=False

     dest2=Destination()
     dest2.name="Hyderabad"
     dest2.img='services2.jpg'
     dest2.desc="Awesome city"
     dest2.price=8000
     dest2.offer=True

     dest3=Destination()
     dest3.name="Bangalore"
     dest3.img='services3.jpg'
     dest3.desc="Beautiful city"
     dest3.price=9000
     dest3.offer=True
     dests=[dest1,dest2,dest3]
    
     return render(request,"index.html",{'dests':dests})