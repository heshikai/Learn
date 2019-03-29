
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import page

urlpatterns = [
    url(r'^(?P<slug>[\w./-]+)/$',page,name='page'),
    url(r'^$',page,name='homepage'),
]
