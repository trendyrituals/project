from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	url(r'^sign_check/$', views.sign_check, name='sign_check'),
	url(r'^register_here/$', views.register_here, name='conregister_here'),
	url(r'^contact/$', views.contact, name='contact_us'),
    url(r'^sign_in/$', views.sign_in, name='sign_in'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^register_student/$', views.register_student, name='register_student'),
    url(r'^register_teacher/$', views.register_teacher, name='register_teacher'),
    url(r'^$', views.index, name='index'),
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)