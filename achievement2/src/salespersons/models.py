from django.db import models
from django.contrib.auth.models import User  # needed for the OneToOneField

# Create your models here.


class Salesperson(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="no bio... start one up!")
    pic = models.ImageField(upload_to='salespersons', default='no_picture.jpg')

    def __str__(self):
        return f"Profile of {self.username}"
        # f-string allows formatting of string
