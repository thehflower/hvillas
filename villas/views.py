from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import  HttpResponseRedirect

from villas.models import Villa,Resident

def index(request):
	return render(request,'index.html',{})

def about(request):
	return render(request,'about.html',{})
def contact(request):
	return render(request,'contact.html',{})
def location(request):
	return render(request,'location.html',{})
def details(request):
        
        available_v=list(Villa.objects.all())
        not_available= []
        for v1 in Villa.objects.all():
                for r1 in Resident.objects.all():
                        if  v1.name == r1.villa.name :
                                 del available_v[available_v.index(v1)]
                                 not_available.append(v1)
        
        return render(request,'details.html',{'available': available_v,'notavailble':not_available})

@login_required (login_url='/login/')
def resident(request):
        r=Resident.objects.get(name = request.user.username)
        return render(request,'resident.html',{'resident':r})

def logout_view(request):
        logout(request)
        return HttpResponseRedirect('/')

