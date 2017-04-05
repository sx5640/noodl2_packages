# coding: utf-8

from django.test import TestCase

from .models import *
from content.models import *

from datetime import datetime
from decimal import Decimal, DecimalException, InvalidOperation
from django.core.exceptions import *
from django.db.utils import IntegrityError

# Create your tests here.
class ModelTest(TestCase):
    #----------------------------------------------------------------------  
    @classmethod
    def setUpTestData(cls):
        description='<img alt="" src="https://cdn0.vox-cdn.com/thumbor/hN4EeREv8bHNymHPOX4RO87efnc=/0x0:2100x1400/1310x873/cdn0.vox-cdn.com/uploads/chorus_image/image/53943747/rebel_haxd.0.jpg" /> <p id="SOvwwY">In April 2000, New Line Cinema released <em>Love &amp; Basketball</em>, the debut film of writer-director Gina Prince-Bythewood. It’s a refreshingly nuanced and original screen romance, a love story spanning more than a decade in the lives of two black basketball players, while encompassing details about gender, race, class, and culture that are clearly drawn from Prince-Bythewood’s personal experiences and observations. Two months later, in June, director John Singleton capped off a decade as one of the most successful black directors in Hollywood by watching his punchy remake of the blaxploitation classic <em>Shaft</em> become a solid box office hit. Those two movies arriving so closely together on the calendar represented a rare encouraging sign from an...</p> <p> <a href="http://www.theverge.com/2017/3/28/15089888/black-film-directors-new-tv-shows-shots-fired-rebel-bythewood-singleton">Continue reading&hellip;</a> </p>',    
        cls.s1 = Source.objects.create(title='the_verge',
                                   url='http://www.theverge.com',
                                   rss='http://www.theverge.com/rss/index.xml')
        cls.a1 = Article.objects.create(title='Our best black filmmakers are finding fresh opportunities on TV',
                                    url='http://www.theverge.com/2017/3/28/15089888/black-film-directors-new-tv-shows-shots-fired-rebel-bythewood-singleton',
                                    author='Noel Murray',
                                    source=cls.s1,
                                    description=description,
                                    publication_time=datetime.now())                 
  
    def test_model_creation(self):
        """test if models can be created"""
         
        k1 = Keyword.objects.create(name = "film")
        ka1 = KeywordAnalysis.objects.create(article = self.a1, keyword = k1, relevance = Decimal(0.5))
  
        return self.assertEqual(
            (Keyword.objects.get(id=k1.id), KeywordAnalysis.objects.get(id=ka1.id)), 
            (k1, ka1)
        )
    
    def test_keyword_analysis_has_greater_than_one_relevance(self):
        """test if models can be created"""
        with self.assertRaises(DecimalException) as ex:
            kw = Keyword.objects.create(name = "film")
            ka = KeywordAnalysis.objects.create(article = self.a1, keyword = kw, relevance = Decimal(5))
                
        return self.assertEqual(type(ex.exception), InvalidOperation)
        
    def test_non_unique_keyword_name(self):
        """test if models can be created"""
        with self.assertRaises(IntegrityError) as ex:
            kw1 = Keyword.objects.create(name = "film")
            kw2 = Keyword.objects.create(name = "film")            
                
        return ex       