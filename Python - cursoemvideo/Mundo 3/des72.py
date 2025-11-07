tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatoze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:

    n1 = int(input('\nDigite um número de 0 à 20 e receba ele por extenso.\nSeu número: '))
    print(f'\n\033[34m{tupla[n1]}\033[m\n')

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar in 'Nn':
        break
    elif continuar in 'Ss':
        continue
    else:
        print('Valor inválido. Programa encerrado.')
        break