from django.shortcuts import render
from Management.models import Category, Students

def CommonData():
    categories = Category.objects.all()
    return {"categories":categories}


def ContactUs(request):
    data = { 
        "title":"Contact @ Fashion Hub"
    }
    s = Students.objects.all()  # select * from table_name --> Return QuerySet
    # s = Students.objects.filter(sem = 4, id = 3) # select * from table_name where `condition` --> Return QuerySet
    # s = Students.objects.get(sem = 4, first_name = 'Raj') # Single Object --> Return Object
    # s = Students.objects.filter(sem = 4).first() # Single Object --> Return Object
    # s = Students.objects.filter(sem = 4).last() # Single Object --> Return Object
    # s = Students.objects.all().count()
    # s = Students.objects.all().values_list('first_name', 'sem')
    # s = Students.objects.all().values('first_name', 'sem')

    categories = Category.objects.all()
    data = { 
        "title":"Contact @ Fashion Hub",
        "students":s,    
    }
    data.update(CommonData())
    return render(request, 'contact.html', data)
