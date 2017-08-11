from django.shortcuts import render
from django.http import HttpResponse
from main_app import views
# Create your views here.

def index(request):
    my_dict = {'insert_me':"Hello I am from views.py xXD"}
    return render(request,'index.html',context = my_dict)
