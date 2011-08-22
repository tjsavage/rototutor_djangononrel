from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

handler500 = 'djangotoolbox.errorviews.server_error'


urlpatterns = patterns('',
    ('^', 'djangoappengine.views.warmup'),
)
