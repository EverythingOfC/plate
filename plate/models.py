from django.db import models

# Create your models here.
class board(models.Model):
  title = models.TextField()
  contents = models.TextField()
  image = models.ImageField(upload_to= 'images/', null=True, black = True)