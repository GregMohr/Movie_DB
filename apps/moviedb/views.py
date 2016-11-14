from django.shortcuts import render

def index(request):
    return render(request,'moviedb/index.html')

def search(request):
    pass
