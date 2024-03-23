from rest_framework.permissions import IsAuthenticated
from apps.core.api.viewsets.base import BaseModelViewSet
from apps.student.api.serializers.student import (
    StudentListSerializer,
    StudentDetailSerializer,
    StudentCreateSerializer,
)
from apps.student.models import Student


class StudentViewSet(BaseModelViewSet):
    model = Student
    permission_classes = [IsAuthenticated]
    serializer_class = StudentListSerializer
    has_file_field = True
    action_serializer_classes = {
        "create": StudentCreateSerializer,
        "retrieve": StudentDetailSerializer,
        "update": StudentCreateSerializer,
        "partial_update": StudentCreateSerializer,
    }
