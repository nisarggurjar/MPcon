from django.shortcuts import render, redirect
from Management.models import Category, ContactForm, SubCategory

def CommonData():
    categories = Category.objects.all()
    subCat = SubCategory.objects.all()
    return {"categories":categories, "subcats":subCat}


def ContactUs(request):
    data = { 
        "title":"Contact @ Fashion Hub",  
    }
    if request.method == "POST":
        data = request.POST
        name = data['name']
        email = data['email']
        msg = data['msg']
        ContactForm.objects.create(name = name, email = email, msg = msg)
        return redirect('home')
    data.update(CommonData())
    return render(request, 'contact.html', data)



    # s = Students.objects.all()  # select * from table_name --> Return QuerySet
    # s = Students.objects.filter(sem = 4, id = 3) # select * from table_name where `condition` --> Return QuerySet
    # s = Students.objects.get(sem = 4, first_name = 'Raj') # Single Object --> Return Object
    # s = Students.objects.filter(sem = 4).first() # Single Object --> Return Object
    # s = Students.objects.filter(sem = 4).last() # Single Object --> Return Object
    # s = Students.objects.all().count()
    # s = Students.objects.all().values_list('first_name', 'sem')
    # s = Students.objects.all().values('first_name', 'sem')