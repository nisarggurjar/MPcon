from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40,null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name +  " <---> " + self.category.name

class Product(models.Model):
    subCat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=True, null=True)
    img1 = models.FileField()
    img2 = models.FileField()
    img3 = models.FileField()
    tagLine = models.CharField(max_length=128, blank=True, null=True)
    price = models.IntegerField()
    description = models.TextField()
    is_avail = models.BooleanField(default=True)
    date_added = models.DateField(auto_now_add=True, null = True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, null = True, blank=True)

    def __str__(self):
        return self.title + " -- " + self.subCat.name

class ContactForm(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    msg = models.TextField(null = True, blank=True)

    def __str__(self):
        return self.name


# class Students(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
#     mobile = models.CharField(max_length=13)
#     id_card = models.FileField()
#     sem = models.IntegerField()
#     roll_no = models.CharField(max_length=20, unique=True)
#     date_of_birth = models.DateField(null = True, blank=True)
#     date_of_joining = models.DateField(auto_now_add=True, null = True, blank=True)
#     last_updated = models.DateTimeField(auto_now=True, null = True, blank=True)

#     def __str__(self):
#         return self.first_name + " --- " + str(self.sem)
