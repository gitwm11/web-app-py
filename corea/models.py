from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    infos = models.TextField()
    descri = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
