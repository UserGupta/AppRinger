from django.db import models

# Create your models here.

class Books(models.Model):
    id 
    smallThumbnail = models.CharField(max_length=122)
    thumbnail = models.CharField(max_length=122)
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=30)
    authors = models.CharField(max_length=122)
    publishedDate = models.DateField
    description = models.CharField(max_length=30)

    def __str__(self):
      return self.title

    




