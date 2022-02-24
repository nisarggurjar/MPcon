from django.shortcuts import render

def ContactUs(request):
    return render(request, 'contact.html')
