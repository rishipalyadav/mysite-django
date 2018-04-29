from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'personal/home.html')
    # return HttpResponse("Hello")
def contact(request):
    return render(request,'personal/basic.html', {'content': ['Please email me at yadav.rishipal001@gmail.com']})
