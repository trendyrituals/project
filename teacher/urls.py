from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^teacher_desk/bid/(?P<id>\d+)/(?P<std>\d+)/$', views.bid, name='bid'),
	url(r'^teacher_desk/view/(?P<id>\d+)/$', views.view_job, name='view_job'),
	url(r'^teacher_desk/search_job/$', views.search_job, name='search_job'),
	url(r'^teacher_desk/degree/$', views.degree_upload, name='degree_upload'),
	url(r'^teacher_desk/bid_manager/$', views.bid_manager, name='bid_manager'),
	url(r'^logout_view/$', views.logout_view, name='logout_view'),
    url(r'^teacher_desk/$', views.teacher_desk, name='teacher_desk'),
]
