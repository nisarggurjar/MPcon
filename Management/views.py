from django.shortcuts import render, redirect
from Management.models import Category, ContactForm, Product, SubCategory

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

def ProductListPage(request, cid):
    
    # sub = SubCategory.objects.get(id = cid)
    # products = Product.objects.filter(subCat__name = name)
    products = Product.objects.filter(subCat_id = cid) #fieldname_id works only for pk with relational object
    data = { 
        "title":"Contact @ Fashion Hub",  
        "products":products
    }
    request.session['user'] = request.user

    print(request.session['user'])
    data.update(CommonData())
    return render(request, 'men.html', data)








    # s = Students.objects.all()  # select * from table_name --> Return QuerySet
    # s = Students.objects.filter(sem = 4, id = 3) # select * from table_name where `condition` --> Return QuerySet
    # s = Students.objects.get(sem = 4, first_name = 'Raj') # Single Object --> Return Object
    # s = Students.objects.filter(sem = 4).first() # Single Object --> Return Object
    # s = Students.objects.filter(sem = 4).last() # Single Object --> Return Object
    # s = Students.objects.all().count()
    # s = Students.objects.all().values_list('first_name', 'sem')
    # s = Students.objects.all().values('first_name', 'sem')
