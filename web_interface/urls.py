from django.conf.urls import url, include
from .views import IndexView, show_users, welcome

urlpatterns = {
	url(r'^show/', show_users, name='show_users_view'),
	url(r'^user/', IndexView.as_view(), name='user_view'),
	url(r'^$', welcome, name='welcome_view'),
}