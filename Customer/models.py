from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=13, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user.username

### Abstract Base Classes

# class CommonInformation(models.Model):
#     name = models.CharField(max_length=128, null=True, blank=True)
#     email = models.EmailField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add= True)
#     update_at = models.DateField(auto_now=True)

#     class Meta:
#         abstract = True

# class Student(CommonInformation):
#     roll_no = models.CharField(max_length=127)

# class Teacher(CommonInformation):
#     emp_no = models.CharField(max_length=127)

### MultiTable Inheritance

class Address(models.Model):
    house_no = models.CharField(max_length=127)
    pin_code = models.CharField(max_length=127)


class Warehouses(Address):
    company = models.CharField(max_length=127)

### Proxy Model Inheritance

