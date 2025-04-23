from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class basefeild(models.Model):
    name = models.CharField(max_length=100,)
    email = models.EmailField()
    phone = models.CharField(max_length=15,)
    address = models.TextField()

    
class student(basefeild):
    roll = models.CharField(max_length=10,)
    course = models.CharField(max_length=100,)
    year = models.IntegerField()
    fees = models.IntegerField()

class employee(basefeild):
    emp_id = models.CharField(max_length=10,)
    designation = models.CharField(max_length=100,)
    salary = models.IntegerField()
    department = models.CharField(max_length=100,)