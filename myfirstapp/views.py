from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .forms import *
from myfirstapp.models import Topic
# Create your views here.

def resume(request):

    return render(request, 'resume.html')



def myfunctioncall(request):
    return HttpResponse("Hello World")



def success(request):
    my_dict = "var1"
    return render(request, 'success.html')

def submitmyform(request):
    mydictionary = {
        "var1" : request.POST['myname'],
        "var2" : request.POST['myemail'],
        "var3" : request.POST['mycountry'],
        "var4" : request.POST['mynumber'],\
        "var5" : request.POST['mytextarea'],
        "method" : request.method
    }
    return render(request, 'success.html', context=mydictionary)
