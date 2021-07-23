from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.CharField(max_length=10)
    ename = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = 'employee'
