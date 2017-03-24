from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Source(models.Model):
    
    #attributes
    title = models.CharField(max_length = 200, db_index = True)
    url = models.URLField(max_length = 400)
    rss = models.URLField(max_length = 400)
    creation_time = models.DateTimeField(auto_now_add = True)
    last_update = models.DateTimeField(null = True)
    
    def __str__(self):
        return self.title.replace('_', ' ').title()
    
class Article(models.Model):
    
    #attributes
    title = models.CharField(max_length = 200)
    url = models.URLField(max_length = 400)
    image_url = models.URLField(max_length = 400)
    author = models.CharField(max_length = 200)
    description = models.TextField()
    publication_time = models.DateTimeField(auto_now_add = True)
    source = models.ForeignKey(Source, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title.replace('_', ' ').title()    
        