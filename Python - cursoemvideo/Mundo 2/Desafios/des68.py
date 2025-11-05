from random import randint

print('\033[40;1m VAMOS JOGAR PAR OU ÍMPAR \033[m')

while True:

    pc = randint(1, 11)
    n1 = int(input('\nDigite um valor: '))
    parimpar = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]

    if (pc + n1) % 2 == 0:
        print(f'\nVocê jogou {n1} e o computador {pc}. Total de {pc + n1}. DEU PAR!')
    else:
        print(f'\nVocê jogou {n1} e o computador {pc}. Total de {pc + n1}. DEU ÍMPAR!')

    if parimpar == 'P' and (n1 + pc) % 2 == 0 or parimpar == 'I' and (n1 + pc) % 2 == 1:
        print('Você VENCEU!')
    elif parimpar == 'P' and (n1 + pc) % 2 == 1 or parimpar == 'I' and (n1 + pc) % 2 == 0:
        print('Você PERDEU!')

    simnao = input('\nVamos jogar novamente? [S/N]: ').strip().upper()
    if simnao == 'N':
        break
    elif simnao == 'S':
        continue

