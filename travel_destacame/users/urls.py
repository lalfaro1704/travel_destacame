from django.conf.urls import url, include

from rest_framework import routers
from rest_framework.authtoken import views as rest_framework_views

from .views import UserViewSet

app_name = "users"

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
	url(r'api/', include(router.urls)),
    url(r'api/get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]
