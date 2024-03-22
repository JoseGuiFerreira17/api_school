from apps.core.api.viewsets import BaseModelViewSet
from apps.student.api.serializers.parent import ParentSerializer
from apps.student.models import Parent


class ParentViewSet(BaseModelViewSet):
    serializer_class = ParentSerializer
    queryset = Parent.objects.all()
