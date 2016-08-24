from django.conf.urls import url

from . import views

# from mobileinfo.views import index

urlpatterns = [
	url(r'^$', views.home, name='home'),
]    