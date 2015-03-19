from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404
from .models import Product

def product( request ):
    productData = get_object_or_404( Product, id=1 )

    return render_to_response('product-data-sheet-product.html', { 'product': productData }, context_instance=RequestContext(request))