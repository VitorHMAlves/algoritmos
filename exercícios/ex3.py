def somaimposto(taxaimposto, custo):
    valor = custo * (taxaimposto / 100)
    valorfinal = custo + valor
    return valorfinal


a = float(input(f'Digite o valor da taxa em %: '))
b = float(input(f'Digite o valor do custo em R$: '))
calculofinal = somaimposto(a, b)
print(f'O valor do produto com {a}% de taxa de imposto é igual a R${calculofinal :.2f}')
