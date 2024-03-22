from rest_framework.serializers import ModelSerializer
from apps.student.models import Parent
from apps.core.api.serializers.address import AddressSerializer


class ParentSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Parent
        fields = [
            "id",
            "mother_name",
            "father_name",
            "phone",
            "address",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
        }
