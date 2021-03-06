from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class ParrotSnacks(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Parrot(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    parrotsnacks = models.ManyToManyField(ParrotSnacks)
    
    def __str__(self):
        return self.name

    class Meta: 
        ordering = ['name']


