from django.shortcuts import render
from  django.http import HttpResponse
# Create your views here.


def calculation(request):
    return render(request, 'cal.html')

def add(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])

    res = n1 + n2

    return render(request,"cal.html" ,{'df':res})


def sub(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])

    res = n1 - n2

    return render(request,"cal.html" ,{'df':res})

    
def mult(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])

    res = n1 * n2

    return render(request,"cal.html" ,{'df':res})


def div(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])

    res = n1 / n2

    return render(request,"cal.html" ,{'df':res})