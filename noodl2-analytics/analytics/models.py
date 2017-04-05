from __future__ import unicode_literals

from django.db import models
from content.models import Article

# Create your models here.
class Keyword(models.Model):
    name = models.CharField(max_length = 200, db_index = True, blank=False, unique=True)
    articles = models.ManyToManyField(Article, through="KeywordAnalysis")
    
    def __str__(self):
        return self.name.replace('_', ' ').title()    
    
########################################################################
class KeywordAnalysis(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    relevance = models.DecimalField(max_digits=10,decimal_places=10)
    
    def __str__(self):
        return self.article.__str__() + ' & ' +  self.keyword.__str__()   

        
        
    
    
    