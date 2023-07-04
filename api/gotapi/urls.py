from rest_framework.routers import DefaultRouter
from django.urls import path, include
from gotapi.views import CharacterViewSet, HouseViewSet

router = DefaultRouter()
router.register(r'characters', CharacterViewSet)
router.register(r'houses', HouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]