from django.conf.urls import url, include

from rest_framework import routers

from .views import (BusViewSet)

router = routers.DefaultRouter()
router.register(r'bus', BusViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
]