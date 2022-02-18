from django.shortcuts import render
from module import *


def index(request):
    return render(request,'index.html')


