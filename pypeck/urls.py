from django.conf.urls import patterns
from django.conf.urls import url

from pypeck.views import PyPeckView

urlpatterns = patterns(
    '',
    url('^$', PyPeckView.as_view(), name='pypeck')
)
