from django.conf.urls import url
from habito_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user', views.show_user, name='user'),
    # url(r'^habit/', views.about, name='habit'),

    url(r'^test_habit/(?P<habit_title_slug>[\w\-]+)/$', views.show_habit, name='habit'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),

]
