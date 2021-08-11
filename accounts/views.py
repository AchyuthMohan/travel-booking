from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
            else:
                user=User.objects.create_user(username=username,email=email,password=password2,first_name=first_name,last_name=last_name)
                user.save();
                print("user created")
            
        else:
            print("password not matching")
            return redirect('register')
        return redirect("/",messages=messages)
        
    else:
        return render(request,"register.html")
