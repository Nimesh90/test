from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    description = models.TextField(max_length=250)
    email = models.TextField(max_length=24)
    startDate = models.DateField(max_length=2)
    endDate = models.DateField(max_length = 2)
    def __str__(self):
            return self.name +" - "+ self.email

