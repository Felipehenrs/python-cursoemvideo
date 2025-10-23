n = 'p'
while n != 'f' and n != 'm':
    n = str(input(f'Informe seu sexo. ("M" para masculino, "F" para feminino): ')).lower().strip()
    if n == 'f':
        print('Sexo feminino registrado com sucesso!')
    elif n == 'm':
        print('Sexo masculino registrado com sucesso!')
    else:
        print('Digite um valor valido!\n')
