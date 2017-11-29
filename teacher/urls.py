from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^teacher_desk/start_project/(?P<id>\d+)/$', views.start_project, name='start_project'),
	url(r'^teacher_desk/upload_solution/upload/(?P<id>\d+)/(?P<job>\d+)/(?P<std>\d+)/$', views.upload_sol, name='upload_sol'),
	url(r'^teacher_desk/upload_solution/$', views.upload_solution, name='upload_solution'),
	url(r'^teacher_desk/bid/(?P<id>\d+)/(?P<std>\d+)/$', views.bid, name='bid'),
	url(r'^teacher_desk/view/(?P<id>\d+)/$', views.view_job, name='view_job'),
	url(r'^teacher_desk/search_job/$', views.search_job, name='search_job'),
	url(r'^teacher_desk/degree/$', views.degree_upload, name='degree_upload'),
	url(r'^teacher_desk/cancel_url_bid/$', views.cancel_url_bid, name='cancel_url_bid'),
	url(r'^teacher_desk/return_url_bid/$', views.return_url_bid, name='return_url_bid'),
	url(r'^teacher_desk/bid_manager/$', views.bid_manager, name='bid_manager'),
	url(r'^logout_view/$', views.logout_view, name='logout_view'),
    url(r'^teacher_desk/$', views.teacher_desk, name='teacher_desk'),
]
