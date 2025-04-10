from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import cover_api, dummy

router = DefaultRouter()
router.register(r'speakers', dummy.SpeakerViewSet)
router.register(r'sessions', dummy.SessionViewSet)
router.register(r'organizations', dummy.OrganizationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Cover API Helpers
    path('cover_session/', cover_api.cover_session),
]
