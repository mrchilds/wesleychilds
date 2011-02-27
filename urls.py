import os

from django.conf.urls.defaults import *

from mainsite.views import *

from django.contrib import admin
admin.autodiscover()

DIRNAME = os.path.dirname(__file__)

urlpatterns = patterns('',
    # Example:
    (r'^$', home),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$','django.views.static.serve',
     {'document_root': os.path.join(DIRNAME, "static"), 'show_indexes': True}),
)
