from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
# from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shop.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url( r'^$'      , RedirectView.as_view(url='home', permanent = False )),

    url(r'^signin/', 'authShop.views.signin', name='signin'),
    url(r'^signup/', 'authShop.views.signup', name='signup'),

    url(r'^product/', 'catProducts.views.product', name='product'),
)
