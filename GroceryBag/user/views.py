from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from dbapp.models import*
from django.db import connection
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def userhome(request):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://localhost:8000/login/')
    s=items.objects.filter(uid=int(request.session['id']))

    return render(request,"user/user_home.html",{'ulist':s})
def add(request):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://localhost:8000/login/')
    if request.method=='POST':
        iname=request.POST.get('iname')
        qnty=request.POST.get('iqnt')
        status=request.POST.get('istatus')
        idate=request.POST.get('idate')
        s=items(item_name=iname,item_q=qnty,status=int(status),gdate=idate,uid_id=int(request.session['id']))
        s.save()
        messages.success(request,'saved!!')
    return render(request,"user/add.html")
def gupdate(request,id):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://localhost:8000/login/')
    s=items.objects.filter(id=id)
    if request.method=='POST':
        iname=request.POST.get('iname')
        qnty=request.POST.get('iqnt')
        status=request.POST.get('istatus')
        idate=request.POST.get('idate')
        items.objects.filter(id=id).update(item_name=iname,item_q=qnty,status=int(status),gdate=idate,uid_id=int(request.session['id']))
        messages.success(request,'Updated!!')

    return render(request,"user/update.html",{'ulist':s})

def filter(request):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://localhost:8000/login/')
    idate=request.POST.get('fdate')
    print(idate)
    s=items.objects.filter(Q(uid=int(request.session['id'])) and Q(gdate=idate))

    return render(request,"user/user_home.html",{'ulist':s})


def delete(request,id):
    keys = request.session.keys()
    if 'id' not in keys:
        messages.success(request, "Session Expired! Please Login Again")
        return redirect('http://localhost:8000/login/')
    if request.method=='POST':
        items.objects.get(id=id).delete()
        return redirect("/userhome")

    return render(request,"user/delete.html")
