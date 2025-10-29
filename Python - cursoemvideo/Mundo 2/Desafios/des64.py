contador = 0
soma = 0
while True:
    n1 = int(input("Digite um número. (999 para parar): "))

    if n1 != 999:
        contador += 1
        soma += n1
    else:
        print(f'Você digitou {contador} múmeros e a soma entre eles é {soma}.')
        break
