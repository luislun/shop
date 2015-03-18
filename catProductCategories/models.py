from django.db import models

class CatProductCategory( models.Model ):
    category = models.CharField( max_length = 100 )
    primary  = models.BooleanField( default = False )
    parent   = models.ForeignKey( "self", related_name = "children", null=True, blank=True )
    
    def __unicode__( self ):
      return self.category


# class CatProductCategoryChild( models.Model ):
#     categoryParent = models.ForeignKey( CatProductCategory, related_name='parent' )
#     categoryChild  = models.ForeignKey( CatProductCategory, related_name='child')
