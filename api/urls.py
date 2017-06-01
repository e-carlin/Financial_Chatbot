from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SMSView, IndexView

urlpatterns = {
    url(r'^api/v1/sms/$', SMSView.as_view(), name='sms-view'),
    url(r'^$', IndexView.as_view(), name='index-view'),
}

urlpatterns = format_suffix_patterns(urlpatterns)