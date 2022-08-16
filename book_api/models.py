from time import timezone
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, null=True)
    number_of_pages = models.IntegerField(null=True)
    published_date = models.DateField(null=True) 
    quantity = models.IntegerField(null=True)

def __str__(self):
    return self.title
