from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^(?P<num>\d+)/$', views.test),
]
