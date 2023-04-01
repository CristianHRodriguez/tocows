from django.urls import path, include
from rest_framework import routers
from .views import PhotoViewSet, CowsViewSet, BornCowsViewSet

router = routers.DefaultRouter()
router.register(r'listas', CowsViewSet)
router.register(r'nacimientos', BornCowsViewSet)
router.register(r'fotos', PhotoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]