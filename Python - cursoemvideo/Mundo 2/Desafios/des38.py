n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'O número \033[32m{n1}\033[m é maior que o número \033[31m{n2}\033[m.')
elif n1 < n2:
    print(f'O número \033[32m{n2}\033[m é maior que o número \033[31m{n1}\033[m.')
else:
    print(f'Os dois valores \033[33msão iguais\033[m, não há um maior que o outro.')