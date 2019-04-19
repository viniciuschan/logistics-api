from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .views import LogisticsNetViewSet


router = DefaultRouter()

router.register(r'v1/logistics', LogisticsNetViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
