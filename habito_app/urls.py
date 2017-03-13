from django.conf.urls import url
from habito_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # I removed this and put it in the habito directory
    # in the book it said to not put it in the app directory
    # url(r'^accounts/', include('registration.backends.simple.urls')),
]
