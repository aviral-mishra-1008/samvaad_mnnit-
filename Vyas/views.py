from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from math import ceil
from Home.models import Submissions


def first(request):
    arts = Post.objects.all()
    n = len(arts)
    for i in arts:
        i.article = i.article[0:255]+"...."
    params={'no_of_arts':n, 'range':range(1,n), 'arts': arts}
    return render(request, "firstpost.html", params)



def allpost(request, slug):
    try:
        return render(request,f"Articles/{slug}.html")
    except:
        return render(request,"erono1.html")


