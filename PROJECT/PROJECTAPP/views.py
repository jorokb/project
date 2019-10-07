from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "PROJECTAPP/hi.html")

def lpc(request):
    return render(request, "PROJECTAPP/lpc.html")

def lpn(request):
    return render(request, "PROJECTAPP/lpn.html")

def lpn2(request):
    return render(request, "PROJECTAPP/lpn2.html")

def lpp(request):
    return render(request, "PROJECTAPP/lpp.html")

def pst(request):
    return render(request, "PROJECTAPP/pst.html")

def pst2(request):
    return render(request, "PROJECTAPP/pst2.html")
