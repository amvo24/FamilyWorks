from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import TaskViewSet

router = SimpleRouter()

router.register(
    r'task',
    TaskViewSet,
    basename='task'
)

urlpatterns = [
    path("", include(router.urls))
]
