from django.urls import include, path

from rest_framework.routers import SimpleRouter

from .views import (
    UserViewSet,
    CustomTokenObtainPairView,
    CurrentUserLoggedIn,
    LogoutView
)
router = SimpleRouter()

router.register(
    r'users',
    UserViewSet,
    basename='user'
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)



urlpatterns = [
    path("", include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('currently_logged_in/', CurrentUserLoggedIn.as_view(), name='current_user_logged_in'),
    path('logout/', LogoutView.as_view(), name="logout")

]
