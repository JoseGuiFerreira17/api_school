from django.contrib import admin
from apps.accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "email", "phone")
    list_filter = ("is_active", "is_staff", "is_superuser")
    readonly_fields = ("id", "created_at", "modified_at")
    fieldsets = (
        ("Informações Básicas", {"fields": ("id", "name", "email", "phone")}),
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
        ("Datas", {"fields": ("created_at", "modified_at")}),
    )
    ordering = ("-created_at",)
    actions = ["activate_users", "deactivate_users"]

    def activate_users(self, request, queryset):
        queryset.update(is_active=True)

    activate_users.short_description = "Ativar usuários"

    def deactivate_users(self, request, queryset):
        queryset.update(is_active=False)

    deactivate_users.short_description = "Desativar usuários"
