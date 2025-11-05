print('\033[40;1m BANCO FELIPE \033[m')

while True:
    valor = int(input('Qual valor você quer sacar? R$'))

    print('\nProcessando...\n')

    if valor >= 100:
        cem = valor // 100
        valor = valor % 100
        print(f'Total de {cem} cédulas de R$100.00')

    if valor >= 50:
        cinquenta = valor // 50
        valor = valor % 50
        print(f'Total de {cinquenta} cédulas de R$50.00')

    if valor >= 20:
        vinte = valor // 20
        valor = valor % 20
        print(f'Total de {vinte} cédulas de R$20.00')

    if valor >= 10:
        dez = valor // 10
        valor = valor % 10
        print(f'Total de {dez} cédulas de R$10.00')

    if valor >= 5:
        cinco = valor // 5
        valor = valor % 5
        print(f'Total de {cinco} cédulas de R$5.00')

    if valor >= 2:
        dois = valor // 2
        valor = valor % 2
        print(f'Total de {dois} cédulas de R$2.00')

    if valor >= 1:
        um = valor // 1
        valor = valor % 1
        print(f'Total de {um} cédulas de R$1.00')

    break

print('\nVolte sempre ao BANCO FELIPE! Tenha um bom dia!')

