from django.urls import path, include
from rest_framework.routers import DefaultRouter

from product.views import CategoryModelViewSet, ProductModelViewSet

router = DefaultRouter()

router.register('category', CategoryModelViewSet)
router.register('', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
