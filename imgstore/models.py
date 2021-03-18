from django.db import models

# Create your models here.
class Userinfo(models.Model):
    username = models.CharField(max_length=75)
    password = models.CharField(max_length=100,default='PASSWORD')
    

class Images(models.Model):
    image_code = models.BinaryField()
    image_type = models.CharField(max_length=20,default=False)
    caption = models.CharField(max_length=100,default='IMG_CAPTION')