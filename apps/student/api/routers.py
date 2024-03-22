from django.urls import path, include
from rest_framework.routers import SimpleRouter

from apps.student.api.viewsets import StudentViewSet, ParentViewSet


router = SimpleRouter()

router.register("students", StudentViewSet, basename="student")
router.register("parents", ParentViewSet, basename="parent")


urlpatterns = [
    path("", include(router.urls)),
]
