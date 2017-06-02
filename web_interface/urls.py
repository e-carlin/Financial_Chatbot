from django.conf.urls import url, include
from .views import IndexView, show_users

urlpatterns = {
	url(r'^show/', show_users, name='show-users-view'),
	url(r'^$', IndexView.as_view(), name='index-view'),
}