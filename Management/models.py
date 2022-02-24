from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40,null=True, blank=True)
    number = models.IntegerField(null=True)
    img = models.FileField()
    disc = models.TextField()
    email = models.EmailField()
    Section = models.ForeignKey()
    test = models.OneToOneField()
