from apps.core.api.viewsets.base import BaseModelViewSet
from apps.student.api.serializers.student import (
    StudentListSerializer,
    StudentDetailSerializer,
    StudentCreateSerializer,
)
from apps.student.models import Student

class StudentViewSet(BaseModelViewSet):
    serializer_class = StudentListSerializer
    queryset = Student.objects.all()
    has_file_field = True
    action_serializer_classes = {
        "create": StudentCreateSerializer,
        "retrieve": StudentDetailSerializer,
        "update": StudentCreateSerializer,
        "partial_update": StudentCreateSerializer,
    }
