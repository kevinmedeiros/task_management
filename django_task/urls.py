from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from core import views


router = routers.DefaultRouter()
router.register(r'task', views.TaskViewSet)
router.register(r'taskgroups', views.TaskGroupViewSet)

urlpatterns = {
    url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
}
