from rest_framework.serializers import ModelSerializer
from apps.student.models import Student
from apps.student.api.serializers.parent import ParentSerializer


class StudentListSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "id",
            "registration",
            "name",
            "gender",
            "birth_date",
            "rg",
            "cpf",
            "file_rg",
            "file_cpf",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
        }


class StudentDetailSerializer(ModelSerializer):
    parent = ParentSerializer()

    class Meta:
        model = Student
        fields = [
            "id",
            "registration",
            "name",
            "gender",
            "birth_date",
            "parent",
            "rg",
            "cpf",
            "file_rg",
            "file_cpf",
            "file_cpf",
        ]


class StudentCreateSerializer(ModelSerializer):
    parent = ParentSerializer()

    class Meta:
        model = Student
        fields = [
            "name",
            "gender",
            "birth_date",
            "parent",
            "rg",
            "cpf",
            "file_rg",
            "file_cpf",
            "file_cpf",
        ]
