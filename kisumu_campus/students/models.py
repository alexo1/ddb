from django.db import models

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    program=models.TextField(max_length=250)
    adm_no=models.CharField(max_length=20)
    dob=models.DateField(default=None)

    def __str__(self):
        return self.first_name+self.last_name