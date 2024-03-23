from rest_framework.serializers import ModelSerializer
from apps.teacher.models import Teacher
from apps.core.api.serializers import AddressSerializer


class TeacherListSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "birth_date",
            "gender",
            "degree",
            "cpf",
            "created_at",
            "modified_at",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
        }

class TeacherCreateSerializer(ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Teacher
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "birth_date",
            "gender",
            "degree",
            "cpf",
            "address",
            "created_at",
            "modified_at",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "modified_at": {"read_only": True},
        }

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        address = AddressSerializer().create(address_data)
        validated_data["address"] = address
        instance = super().create(validated_data)
        instance.associate = True
        instance.save()
        return instance