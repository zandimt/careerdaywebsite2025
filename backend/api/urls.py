from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SpeakerViewSet, SessionViewSet, OrganizationViewSet

router = DefaultRouter()
router.register(r'speakers', SpeakerViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'organizations', OrganizationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
