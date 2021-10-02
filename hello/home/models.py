from django.db import models

# Create your models here.
class url_v(models.Model):
    url = models.CharField(max_length=122)
    date = models.DateField()

def __str__(self):
    return self.name

