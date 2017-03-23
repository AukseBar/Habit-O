from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from habito_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^habito_app/', include('habito_app.urls')),
    # above maps any URLs starting with habito_app/ to be handled by
    # the habito_app application
    url(r'^admin/', admin.site.urls),
	
	# AJAX URLS
	 url(r'^habits/update_habit/toogle_day/$', views.toogle_day, name='toogle_day'),
	 url(r'^habits/update_habit/edit_title/$', views.edit_title, name='edit_title'),
	 url(r'^habits/update_habit/set_today/$', views.set_today, name='set_today'),
]
