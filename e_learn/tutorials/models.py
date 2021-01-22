from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class Books(models.Model):
    priority_status = (
        ('Beginner','Beginner'),
        ('Intermediate','Intermediate'),
        ('Advanced','Advanced'),
    )

    bTitle = models.CharField(max_length=200)
    bImage = models.ImageField(upload_to='Images')
    book = models.FileField(upload_to='books')
    author = models.CharField(max_length=150)
    bDescip = models.CharField(max_length=1000)

    def __str__(self):
        return self.bTitle

class Videos(models.Model):
    priority_status = (
        ('Beginner','Beginner'),
        ('Intermediate','Intermediate'),
        ('Advanced','Advanced'),
    )
    vName = models.CharField(max_length=200)
    vUrl = EmbedVideoField(blank=True)
    vDescip = models.CharField(max_length=1000)
    vCreator = models.CharField(max_length=100)
    
    def __str__(self):
        return self.vName
