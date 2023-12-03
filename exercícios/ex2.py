def p_ou_n():
    a = int(input(f'Entre com um valor: '))
    return a


res = p_ou_n()

if res > 0:

    print('P')
else:
    print('N')
