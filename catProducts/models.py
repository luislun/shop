#encoding:utf-8

from django.db import models
from catBrands.models import CatBrand
from catProductCategories.models import CatProductCategory 
from productFeatures.models import ProductFeatures
from comments.models import Comment
from photos.models import Photo

class Product( models.Model ):
    product          = models.CharField( max_length=100 )
    description      = models.CharField( max_length=250, null=True, blank=True )
    long_description = models.TextField( null=True, blank=True  )
    price            = models.DecimalField( max_digits=20, decimal_places=6 )
    brand            = models.ForeignKey( CatBrand )
    category_level_1 = models.ForeignKey( CatProductCategory, related_name='category_level_1' )
    category_level_2 = models.ForeignKey( CatProductCategory, related_name='category_level_2', null=True, blank=True )
    category_level_3 = models.ForeignKey( CatProductCategory, related_name='category_level_3', null=True, blank=True )
    category_level_4 = models.ForeignKey( CatProductCategory, related_name='category_level_4', null=True, blank=True )
    category_level_5 = models.ForeignKey( CatProductCategory, related_name='category_level_5', null=True, blank=True )
    features         = models.ManyToManyField( ProductFeatures, null=True, blank=True )
    comments         = models.ManyToManyField( Comment, null=True, blank=True )
    photos           = models.ManyToManyField( Photo, null=True, blank=True )
    relatedProducts  = models.ManyToManyField( 'self', related_name='related_products', null=True, blank=True )

    def __unicode__( self ):
      return self.product