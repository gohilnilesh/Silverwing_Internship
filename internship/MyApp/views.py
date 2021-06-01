from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is a home Page")

def home(request):
    return render(request,"index.html")