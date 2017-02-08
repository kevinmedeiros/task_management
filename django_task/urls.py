from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from core import views
from django.contrib.auth import views as auth_views


router = routers.DefaultRouter()
router.register(r'task', views.TaskViewSet)
router.register(r'taskgroups', views.TaskGroupViewSet)

urlpatterns = {
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
}
