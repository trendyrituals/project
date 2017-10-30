from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^student_desk/delete/(?P<id>\d+)/$', views.delete_job, name='delete_job'),
	url(r'^student_desk/view/(?P<id>\d+)/$', views.view_job, name='view_job'),
	url(r'^student_desk/active_job/$', views.active_job, name='active_job'),
	url(r'^student_desk/create_job/$', views.createjob, name='create_job'),
	url(r'^logout_view/$', views.logout_view, name='logout_view'),
    url(r'^student_desk/$', views.student_desk, name='student_desk'),

]