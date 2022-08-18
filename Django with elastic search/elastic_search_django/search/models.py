from django.db import models

# Create your models here.
class ElasticDemo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=255 )

    def __str__(self):
        return self.title

# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField( )