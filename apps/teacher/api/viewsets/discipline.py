from rest_framework.permissions import IsAuthenticated
from apps.core.api.viewsets import BaseModelViewSet
from apps.teacher.models import Discipline
from apps.teacher.api.serializers import DisciplineSerializer


class DisciplineViewSet(BaseModelViewSet):
    model = Discipline
    permission_classes = [IsAuthenticated]
    serializer_class = DisciplineSerializer
