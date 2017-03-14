from django.conf.urls import url
from habito_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # url(r'^habit/', views.about, name='habit'),

    url(r'^habit/(?P<habit_title_slug>[\w\-]+)/$', views.show_habit, name='show_habit'),
]
