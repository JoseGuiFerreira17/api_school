from django.urls import path, include


urlpatterns = [
    path("", include("apps.docs_urls")),
    path("student/", include("apps.student.api.routers")),
]
