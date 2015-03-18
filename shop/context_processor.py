from catProductCategories.models import CatProductCategory

def categories( request ):
    listCategories = CatProductCategory.objects.filter( primary = True )

    contextData = {
        'listCategories': listCategories,
    }

    return contextData