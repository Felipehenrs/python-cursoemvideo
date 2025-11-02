quercontinuar = 'nada'
acumulador = 0
soma = 0
maior = 0
menor = 0
while quercontinuar != 'n':
    acumulador += 1
    n1 = int(input('Digite um número: '))
    soma += n1
    if n1 > maior:
        maior = n1
    if menor == 0:
        menor = n1
    if n1 < menor:
        menor = n1

    while True:
        quercontinuar = str(input('Quer continuar? [S/N] ')).strip().lower()
        if quercontinuar != 's' and quercontinuar != 'n':
            print('\033[31;1mDigite um valor válido!\033[m')
        else:
            break
print(f'Você digitou {acumulador} números e a média foi {soma/acumulador:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')