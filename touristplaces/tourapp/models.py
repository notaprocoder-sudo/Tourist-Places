from django.db import models

# Create your models here.

class spots(models.Model):
    name = models.CharField(max_length=100)
    known = models.TextField(max_length=500,default='')
    desc = models.TextField()
    thb = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name