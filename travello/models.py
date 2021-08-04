from django.db import models


# Create your models here.
class Destination:
    id:int
    name:str
    desc:str
    price:int
    offer:bool