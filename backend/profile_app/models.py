from django.db import models

# Create your models here.

class Profile(models.Model):
    name=models.CharField(max_length=256)
    profile_image=models.ImageField('images/')
    
    def __str__(self):
        return self.name
    