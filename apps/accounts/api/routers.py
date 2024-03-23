from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apps.accounts.api.viewsets import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = SimpleRouter()

router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]