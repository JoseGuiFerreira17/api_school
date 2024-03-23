from apps.teacher.models import Teacher
from apps.teacher.api.serializers import TeacherCreateSerializer, TeacherListSerializer
from apps.core.api.viewsets import BaseModelViewSet


class TeacherViewSet(BaseModelViewSet):
    model = Teacher
    serializer_class = TeacherListSerializer
    action_serializer_classes = {
        "create": TeacherCreateSerializer,
        "update": TeacherCreateSerializer,
        "partial_update": TeacherCreateSerializer,
    }
