from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^student_desk/cancel_payment/$', views.cancel_payment, name='cancel_payment'),
	url(r'^student_desk/success_payment/$', views.success_payment, name='success_payment'),
	url(r'^student_desk/payment/(?P<id>\d+)/$', views.payment, name='payment'),
	url(r'^student_desk/download_solution/(?P<id>\d+)/$', views.download_solution, name='download_solution'),
	url(r'^student_desk/get_solution/$', views.get_solution, name='get_solution'),
	url(r'^student_desk/bid/delete/(?P<id>\d+)/$', views.delete_bid, name='delete_bid'),
	url(r'^student_desk/bid/(?P<id>\d+)/$', views.view_bid, name='view_bid'),
	url(r'^student_desk/delete/(?P<id>\d+)/$', views.delete_job, name='delete_job'),
	url(r'^student_desk/view/(?P<id>\d+)/$', views.view_job, name='view_job'),
	url(r'^student_desk/active_job/$', views.active_job, name='active_job'),
	url(r'^student_desk/create_job/$', views.createjob, name='create_job'),
	url(r'^logout_view/$', views.logout_view, name='logout_view'),
    url(r'^student_desk/$', views.student_desk, name='student_desk'),

]