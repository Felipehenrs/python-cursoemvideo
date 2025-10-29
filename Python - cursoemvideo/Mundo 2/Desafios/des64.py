contador = 0
soma = 0
while True:
    n1 = int(input("Digite um número. (999 para parar): "))
    contador += 1

    if n1 != 999:
        soma += n1
    else:
        contador -= 1
        print(f'Você digitou {contador} múmeros e a soma entre eles é {soma}.')
        break
