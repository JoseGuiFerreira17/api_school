from rest_framework.serializers import ModelSerializer
from apps.teacher.models import Discipline


class DisciplineSerializer(ModelSerializer):
    class Meta:
        model = Discipline
        fields = "__all__"
        extra_kwargs = {
            "id": {"required": True},
        }
