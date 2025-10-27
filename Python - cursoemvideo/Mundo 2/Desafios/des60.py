acumulador = 1

while True:
    numero = int(input('Digite um número para saber seu fatorial (ou 0 para sair): '))

    if numero < 0:
        print('\n\033[31;1mFatorial só pode ser calculado com números naturais (0 ou maiores).\n\033[m')
        continue
    if numero == 0:
        print('0! = 1')
        break
    print(f'Calculando {numero}! = ', end='')

    for c in range(numero, 0, -1):
        print(f'{c}', end='')
        if c > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
        acumulador *= c

    print(acumulador)
    break

