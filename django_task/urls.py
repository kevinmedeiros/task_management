from django.conf.urls import url
from django.contrib import admin
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = {
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
}
