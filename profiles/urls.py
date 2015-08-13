from django.conf.urls import url
from . import views

urlpatterns = [    
    url(r'^users$', views.index, name='index'),
	# url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]