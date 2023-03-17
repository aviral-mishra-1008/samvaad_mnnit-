from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome")
    # return render(request, "Vyas/home.html")
# Create your views here.