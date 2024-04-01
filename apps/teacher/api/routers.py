from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.teacher.api.viewsets import TeacherViewSet
from apps.teacher.api.viewsets import DisciplineViewSet


router = SimpleRouter()

router.register("teachers", TeacherViewSet, basename="teacher")
router.register("disciplines", DisciplineViewSet, basename="discipline")


urlpatterns = [
    path("", include(router.urls)),
]
