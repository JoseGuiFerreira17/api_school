from django.contrib import admin
from apps.student.models import Student, Parent


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    model = Parent
    list_display = ["mother_name", "father_name", "phone"]
    search_fields = ["mother_name", "father_name", "phone"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ["name", "gender", "registration", "age"]
    search_fields = ["name", "registration"]
    fieldsets = [
        ("Informações básicas", {"fields": ["name", "gender", "registration", "birth_date"]}),
        ("Documentos", {"fields": ["cpf", "rg", "file_cpf", "file_rg"]}),
        ("Responsável", {"fields": ["parent"]}),
    ]
