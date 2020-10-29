from django.http import request
from django.shortcuts import render, HttpResponse,redirect
from .models import Show
def index(request):
    return redirect("/showlist") 

def show_list(request):
    print(request.POST)
    context = {
        'allshows': Show.objects.all()
        
    }
    
    return render(request,"shows.html",context)


def add_show(request):
    Show.objects.create(title=request.POST['title'], network=request.POST['network'])
    
    return redirect("/showlist")

def show_select(request, showId):
    context = {
        'selectedshow': Show.objects.get(id=showId),
        
    }
    
    return render(request, "shows.html", context)