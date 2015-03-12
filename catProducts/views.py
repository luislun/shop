from django.shortcuts import render_to_response
from django.template.context import RequestContext


def product( request ):
    return render_to_response('product-centered.html', {'poll': 'Hola mundo'}, context_instance=RequestContext(request))