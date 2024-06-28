from django.urls import include, path

from rest_framework.routers import SimpleRouter

from .views import (
    FamilyViewSet
)

router = SimpleRouter()

router.register(
    r'family',
    FamilyViewSet,
    basename="family"
)

urlpatterns = [
    path("", include(router.urls)),
]
