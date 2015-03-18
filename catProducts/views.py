from django.shortcuts import render_to_response
from django.template.context import RequestContext


def product( request ):
    return render_to_response('product-data-sheet-product.html', {}, context_instance=RequestContext(request))