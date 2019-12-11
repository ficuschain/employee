from django.db import models

# Create your models here.

class Employee(models.Model):
    id=models.AutoField
    name=models.CharField(max_length=120)
    position=models.CharField(max_length=120)
    salary=models.IntegerField(max_length=2040)

    def __str__(self):
        return self.name
   


