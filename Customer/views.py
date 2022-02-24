from django.shortcuts import render
from django.http import HttpResponse
from Management.views import CommonData
# def Home(request):
#     return HttpResponse("<h2>Hello World</h2><p>How are you?</p>")

def Home(request):
    data = { 
        "title":"Fashion Hub"
    }
    data.update(CommonData())
    return render(request, 'index.html',data)
