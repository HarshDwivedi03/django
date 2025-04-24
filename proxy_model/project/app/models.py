from django.db import models

# Create your models here.
class Baseinfo(models.Model):
    name =models.CharField(max_length=50)
    dob =models.DateField()
    address =models.CharField(max_length=50)
    branch =models.CharField(max_length=50)
    fees =models.IntegerField()

    class Meta:
        db_table='student'
        ordering=['id']
        verbose_name ="My custom Model"
        verbose_name_plural ="My custom Model"


class Studentproxt(Baseinfo):
    class Meta:
        proxy=True