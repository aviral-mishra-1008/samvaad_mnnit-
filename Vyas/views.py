from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from math import ceil


def first(request):
    arts = Post.objects.all()
    n = len(arts)
    nArts= n//4 + ceil((n/4) - (n//4))
    params={'no_of_arts':nArts, 'range':range(1,nArts), 'arts': arts}
    return render(request, "firstpost.html", params)



def allpost(request, slug):
    try:
        return render(request,f"{slug}.html")
    except:
        return render(request,"erono1.html")


