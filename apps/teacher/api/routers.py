from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.teacher.api.viewsets import TeacherViewSet


router = SimpleRouter()

router.register("teachers", TeacherViewSet, basename="teacher")

urlpatterns = [
    path("", include(router.urls)),
]
