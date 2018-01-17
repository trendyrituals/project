from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^superuser/reject_degree/(?P<id>\d+)/$', views.reject_degree, name='reject_degree'),
	url(r'^superuser/accept_degree/(?P<id>\d+)/$', views.accept_degree, name='accept_degree'),
	url(r'^superuser/view_normal_degree/(?P<id>\d+)/$', views.view_normal_degree, name='view_normal_degree'),
	url(r'^superuser/view_degree/(?P<id>\d+)/$', views.view_degree, name='view_degree'),
	url(r'^superuser/rejected_degrees/$', views.rejected_degrees, name='rejected_degrees'),
	url(r'^superuser/accepted_degrees/$', views.accepted_degrees, name='accepted_degrees'),
	url(r'^superuser/new_degrees/$', views.new_degrees, name='new_degrees'),
	url(r'^superuser/view_solution/(?P<id>\d+)/$', views.view_solution, name='view_solution'),
	url(r'^superuser/closed_solution/$', views.closed_solution, name='closed_solution'),
	url(r'^superuser/new_solution/$', views.new_solution, name='new_solution'),
	url(r'^superuser/view_bid/(?P<id>\d+)/$', views.view_bid, name='view_bid'),
	url(r'^superuser/closed_bids/$', views.closed_bids, name='closed_bids'),
	url(r'^superuser/completed_bids/$', views.completed_bids, name='completed_bids'),
	url(r'^superuser/accepted_bids/$', views.accepted_bids, name='accepted_bids'),
	url(r'^superuser/active_bids/$', views.active_bids, name='active_bids'),
	url(r'^superuser/view_project/(?P<id>\d+)/$', views.view_project, name='view_project'),
	url(r'^superuser/closed_projects/$', views.closed_projects, name='closed_projects'),
	url(r'^superuser/under_process_projects/$', views.under_process_projects, name='under_process_projects'),
	url(r'^superuser/active_projects/$', views.active_projects, name='active_projects'),
	url(r'^logout_view/$', views.logout_view, name='logout_view'),
    url(r'^superuser/$', views.superuser_desk, name='superuser_desk'),

]