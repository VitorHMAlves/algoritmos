import random


def embaralhaPalavra(palavra):
    arrayPos = []
    tamanho = len(palavra)
    for i in range(0, tamanho):
        arrayPos.append(i)
    for i in range(0, tamanho):
        pos1 = random.randint(0, tamanho - 1)
        pos2 = random.randint(0, tamanho - 1)

        aux = arrayPos[pos1]
        arrayPos[pos1] = arrayPos[pos2]
        arrayPos[pos2] = aux

    retorno = ''
    for i in arrayPos:
        retorno += palavra[i]

    return retorno.upper()

# Fluxo Principal
palavra = input('Informe uma palavra: ')
print(embaralhaPalavra(palavra))