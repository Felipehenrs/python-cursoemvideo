from random import randint

print('\033[40mJOGO JOKENPO😁\033[m')
opcoes = ['✂️', '📃', '🪨']
bot = randint(0, 2)

while True:
    userentrada = input(f'''\033[1mHora de jogar Jokenpo!\033[m
    Digite "\033[1;32m0\033[m" para {opcoes[0]}
    Digite "\033[1;33m1\033[m" para {opcoes[1]}
    Digite "\033[1;31m2\033[m" para {opcoes[2]}
    Sua escolha: ''').strip()

    if userentrada.isdigit() and '.' not in userentrada:
        user = int(userentrada)
        if user not in [0, 1, 2]:
            print('\033[1;31mDIGITE APENAS O SOLICITADO.\033[m')
        else:
            print(f'\nO BOT escolheu {opcoes[bot]}')
            print(f'Você escolheu {opcoes[user]}')

            if bot == user:
                print(f'🤝 \033[1;33mEMPATE!\033[m')
            elif (bot == 0 and user == 1) or \
                 (bot == 1 and user == 2) or \
                 (bot == 2 and user == 0):
                print(f'😭 \033[1;31mVOCÊ PERDEU!\033[m')
            else:
                print(f'🎉 \033[1;32mVOCÊ VENCEU!\033[m')
                break
    else:
        print('\033[1;31mDIGITE APENAS O SOLICITADO.\033[m')

