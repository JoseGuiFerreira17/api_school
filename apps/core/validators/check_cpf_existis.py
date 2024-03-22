def check_cpf_in_student(cpf):
    from apps.student.models.student import Student

    return True if Student.objects.filter(cpf=cpf).exists() else False
