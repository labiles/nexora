from django.db import models

# Create your models here.


class Sample(models.Model):
    name=models.CharField(max_length=120)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()