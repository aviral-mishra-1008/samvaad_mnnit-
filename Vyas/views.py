from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from math import ceil


def first(request):
    arts = Post.objects.all()
    n = len(arts)
    params={'no_of_arts':n, 'range':range(1,n), 'arts': arts}
    return render(request, "firstpost.html", params)



def allpost(request, slug):
    try:
        return render(request,f"{slug}.html")
    except:
        return render(request,"erono1.html")


