from django.shortcuts import render
from django.http import HttpResponse

# def Home(request):
#     return HttpResponse("<h2>Hello World</h2><p>How are you?</p>")

def Home(request):
    return render(request, 'index.html')
