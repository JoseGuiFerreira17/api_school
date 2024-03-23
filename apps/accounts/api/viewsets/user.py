from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.accounts.api.serializers import (
    UserUpdatePasswordSerializer,
    UserCreateSerializer,
    UserListSerializer,
)
from apps.accounts.models import User
from apps.core.api.viewsets import BaseModelViewSet


class UserViewSet(BaseModelViewSet):
    model = User
    permission_classes = [IsAuthenticated]
    serializer_class = UserListSerializer
    action_serializer_classes = {
        "create": UserCreateSerializer,
        "update": UserUpdatePasswordSerializer,
        "partial_update": UserCreateSerializer,
        "password": UserUpdatePasswordSerializer,
        "me": UserListSerializer,
    }

    @action(detail=False, methods=["get", "put"])
    def me(self, request, *args, **kwargs):
        user = request.user
        if self.request.method == "GET":
            return Response(self.get_serializer(user).data)
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=False, methods=["put"])
    def password(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
