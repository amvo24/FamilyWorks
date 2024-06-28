from django.urls import include, path

from rest_framework.routers import SimpleRouter

from .views import (
    FamilyViewSet,
    FamilyMembershipViewSet,
    InvitationViewSet
)

router = SimpleRouter()

router.register(
    r'family',
    FamilyViewSet,
    basename="family"
)

router.register(
    r'familymembership',
    FamilyMembershipViewSet,
    basename="membership"
)

router.register(
    r'invitation',
    InvitationViewSet,
    basename="invitation"
)



urlpatterns = [
    path("", include(router.urls)),
]
