#encoding:utf-8

from django.db import models

class CatCompany( models.Model ):
    ACTIVE = 'A'
    INACTIVE = 'I'
    IN_PROCESS = 'P'

    STATUS = (
        ( 'A', 'Activo' ),
        ( 'I', 'Inactivo' ),
        ( 'P', 'En Proceso de activación' ),
    )

    company       = models.CharField( max_length=200 )
    rfc           = models.CharField( max_length=15 )
    description   = models.TextField()
    register_date = models.DateTimeField( auto_now=True )
    modify_date   = models.DateTimeField()
    due_date      = models.DateTimeField()
    status        = models.CharField( max_length=1, choices=STATUS, default=IN_PROCESS )
    web           = models.URLField()

    def __unicode__( self ):
      return self.company