from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

handler500 = 'djangotoolbox.errorviews.server_error'

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^admin/', include(admin.site.urls)),
	('^apply/$', 'users.views.apply'),
	('^apply/thanks/$', direct_to_template, {'template': 'apply_thanks.html'}),
	('^account/', include('registration.backends.simple.urls')),
	('^me/$', 'users.views.me'),
    ('^$', direct_to_template, {'template': 'home.html'}),
)
