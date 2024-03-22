from django.core.exceptions import ValidationError
from apps.core.validators.check_cpf_existis import check_cpf_in_student


def validate_cpf(value):
    """
    Função de validação de CPF.
    """
    cpf = "".join(filter(str.isdigit, value))
    if len(cpf) != 11:
        raise ValidationError("CPF deve ter 11 dígitos")

    # Verificar se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        raise ValidationError('CPF inválido')
    
    # Calcular dígitos verificadores
    sum = 0
    weights = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(9):
        sum += int(cpf[i]) * weights[i]
    remainder = sum % 11
    if remainder < 2:
        digit1 = 0
    else:
        digit1 = 11 - remainder

    sum = 0
    weights = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    for i in range(10):
        sum += int(cpf[i]) * weights[i]
    remainder = sum % 11
    if remainder < 2:
        digit2 = 0
    else:
        digit2 = 11 - remainder

     # Verificar se os dígitos verificadores estão corretos
    if int(cpf[9]) != digit1 or int(cpf[10]) != digit2:
        raise ValidationError('CPF inválido')
    
    if check_cpf_in_student(value):
        raise ValidationError("CPF já cadastrado")

    return value
