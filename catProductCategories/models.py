from django.db import models

class CatProductCategory( models.Model ):
    category       = models.CharField( max_length = 50 )
    parentCategory = models.ForeignKey( 'self' )

    def __unicode__( self ):
      return self.category