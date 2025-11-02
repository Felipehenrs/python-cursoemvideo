contador = numeros = 0
while True:
    contador += 1
    n1 = int(input(f'Digite o {contador} número. (Digite "999" para parar): '))
    print('ARMAZENANDO...\n')
    if n1 == 999:
        contador -= 1
        break
    numeros += n1
print(f'Você digitou {contador} números, a soma deles é {numeros}.')

