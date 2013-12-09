from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()
from rest_framework import routers

from taxitogether.views.duck import DuckViewSet


router = routers.DefaultRouter()
router.register(r'ducks', DuckViewSet)

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='base.html')),
    url(r'^api/', include(router.urls)),

    # Examples:
    # url(r'^$', 'taxitogether.views.home', name='home'),
    # url(r'^taxitogether/', include('taxitogether.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
