from statistics import mode
from tabnanny import verbose
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40,null=True, blank=True)
    alias = models.CharField(max_length=30,null=True, blank=True)
    
    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Categories"


class Students(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=13)
    id_card = models.FileField()
    sem = models.IntegerField()
    roll_no = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField(null = True, blank=True)
    date_of_joining = models.DateField(auto_now_add=True, null = True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, null = True, blank=True)

    def __str__(self):
        return self.first_name + " --- " + str(self.sem)