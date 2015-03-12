#encoding:utf-8

from django.db import models
from catBrands.models import CatBrand
from catProductCategories.models import CatProductCategory 

class Product( models.Model ):
    product     = models.CharField( max_length=200 )
    description = models.TextField()
    price = models.DecimalField( max_digits=20, decimal_places=6 )
    
    brand       = models.ForeignKey( CatBrand )
    category_level_1 = models.ForeignKey( CatProductCategory, related_name='category_level_1' )
    category_level_2 = models.ForeignKey( CatProductCategory, related_name='category_level_2', null=True, blank=True )
    category_level_3 = models.ForeignKey( CatProductCategory, related_name='category_level_3', null=True, blank=True )
    category_level_4 = models.ForeignKey( CatProductCategory, related_name='category_level_4', null=True, blank=True )
    category_level_5 = models.ForeignKey( CatProductCategory, related_name='category_level_5', null=True, blank=True )

    def __unicode__( self ):
      return self.product