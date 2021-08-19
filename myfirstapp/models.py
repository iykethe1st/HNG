from django.db import models

# Create your models here.
class Topic(models.Model):
    top_name = models.CharField(max_length = 168, unique = True )

    def __str__(self):
        return selt.top_name

class WebInfo(models.Model):
    message = models.CharField(max_length=400)
    number = models.IntegerField(max_length = 128, unique=True)
    email = models.EmailField(max_length= 128, unique = True)

    def __str__(self):
        return self.name
