from django.shortcuts import render


def accident(request):
    return render(request,'accident.html')