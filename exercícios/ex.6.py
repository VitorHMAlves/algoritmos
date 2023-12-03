def quantidadeDigitos(digito):
    if (digito == 0):
        return 0
    return 1 + quantidadeDigitos(int(digito / 10))

digito = int(input('Informe um número inteiro: '))
print(f'O número {digito} possui {quantidadeDigitos(digito)} digitos.')