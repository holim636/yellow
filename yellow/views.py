from django.shortcuts import render
from module import *


def index(request):
    return render(request,'index.html')
def accident(request):
    return render(request,'accident.html')
def yellowloc(request):
    return render(request,'yellowloc.html')
def yellowaccident(request):
    return render(request,'yellowaccident.html')
def conclusion(request):
    return render(request,'conclusion.html')


