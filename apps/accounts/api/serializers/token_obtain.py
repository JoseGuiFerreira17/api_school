from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer as BaseTokenObtainPairSerializer,
)


class TokenObtainPairSerializer(BaseTokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = self.user.teacher_user_serializer_class
        user = self.user.teacher_user
        if not user:
            user = self.user
        user_data = serializer(user).data
        data.update({"user": user_data})
        return data
