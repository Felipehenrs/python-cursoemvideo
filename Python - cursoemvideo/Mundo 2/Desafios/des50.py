print('\033[1;40mPROGRAMA QUE SOMA NÚMEROS ÍMPARES!\033[m\n')

soma = 0
cont = 0
cont1 = 0

for i in range(1, 7):
    n = int(input(f'Digite o {i}º número inteiro: '))
    if n % 2 == 0:
        soma += n
        cont1 += 1
    cont += 1
print(f'Você digitou {cont} números, desses {cont}, {cont1} eram números pares.'
      f' A soma dos números pares é {soma}.')





