from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IndexViewSet, DailyPriceViewSet

router = DefaultRouter()
router.register(r'indices', IndexViewSet, basename='index')
router.register(r'daily-prices', DailyPriceViewSet, basename='dailyprice')

urlpatterns = [
    path('', include(router.urls)),
]
