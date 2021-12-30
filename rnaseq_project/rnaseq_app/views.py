from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,"rnaseq_app/index.html")

def about(request):
    return render(request,"rnaseq_app/about.html")