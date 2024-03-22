from rest_framework.serializers import ModelSerializer
from apps.core.models import Address


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "street",
            "number",
            "neighborhood",
            "city",
            "state",
            "zip_code",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
        }
