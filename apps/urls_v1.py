from django.urls import path, include


urlpatterns = [
    path("", include("apps.docs_urls")),
    path("", include("apps.student.api.routers")),
    path("", include("apps.accounts.api.routers")),
    path("", include("apps.teacher.api.routers")),
]
