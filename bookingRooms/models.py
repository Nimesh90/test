from django.db import models

# Create your models here.
class book(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=12)
    # description = models.TextField(max_length=250)
    # email = models.TextField(max_length=24)
    # startDate = models.DateField(max_length=2)
    # endDate = models.DateField(max_length = 2)

