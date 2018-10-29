from django.conf.urls import url, include

from rest_framework import routers

from .views import (BusViewSet, TripViewSet, TripStatsViewSet)

router = routers.DefaultRouter()
router.register(r'bus', BusViewSet)
router.register(r'trip', TripViewSet)
router.register(r'tripstats', TripStatsViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
]