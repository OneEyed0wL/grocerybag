from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from dbapp.models import*
from django.db import connection
from django.contrib import messages
from django.db.models import Q
# Create your views here.
def home(request):
    for key in list(request.session.keys()):
        if not key.startswith("_"):  # skip keys set by the django system
            del request.session[key]
    return render(request,"home/homepage.html")

def user_regs(request):
    for key in list(request.session.keys()):
        if not key.startswith("_"):  # skip keys set by the django system
            del request.session[key]
    if request.method=="POST":
        name=request.POST.get('name')
        mail=request.POST.get('email')
        pwd=request.POST.get('password')
        q=user_reg.objects.filter(email=mail).count()
        if q==0:
            s=user_reg(name=name,email=mail,pwd=pwd)
            s.save()
            messages.success(request,"Registration Successful")
        else:
            messages.error(request,"Email Already Exist!")
            

    return render(request,"home/user_reg.html")

def login(request):
    for key in list(request.session.keys()):
        if not key.startswith("_"):  # skip keys set by the django system
            del request.session[key]
    if request.method == 'POST':
        email= request.POST.get('email')
        pwd =request.POST.get('pass')
        z=user_reg.objects.filter(Q(email=email) & Q(pwd=pwd))
        if z.count() > 0:
            for s in z:
                request.session['id']=s.id
                print("\n",s.id,s.name)
                return redirect('http://localhost:8000/userhome/')
                
        else:
            messages.error(request,"Invalid Username or Password")
    return render(request,"home/login.html")