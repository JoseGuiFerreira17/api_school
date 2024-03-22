from django.contrib import admin
from apps.teacher.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "degree", "phone", "cpf",)
    list_filter = ("is_active", "is_staff")
    readonly_fields = ("id", "created_at", "modified_at")
    fieldsets = (
        ("Informações Básicas", {"fields": ( "name", "cpf", "birth_date", "gender", "degree", "email", "phone", "address")}),
        (
            "Permissões",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        ("Senha", {"fields": ("password", )}),
    )
    ordering = ("-created_at",)
    actions = ["activate_teachers", "deactivate_teachers"]

    def activate_teachers(self, request, queryset):
        queryset.update(is_active=True)

    activate_teachers.short_description = "Ativar professores"

    def deactivate_teachers(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_teachers.short_description = "Desativar professores"



