from rest_framework.permissions import IsAuthenticated
from apps.core.api.viewsets import BaseModelViewSet
from apps.student.api.serializers.parent import ParentSerializer
from apps.student.models import Parent


class ParentViewSet(BaseModelViewSet):
    model = Parent
    permission_classes = [IsAuthenticated]
    serializer_class = ParentSerializer
