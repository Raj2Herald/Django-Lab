from django.http import HttpResponse
from django.shortcuts import render

def view_helloworld(request):
    return render(request,'index.html')

def view_helloworld_again(request):
    return render(request,'index2.html')