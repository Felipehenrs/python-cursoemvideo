from random import randint
numeroescolhido = randint(1, 100)
tentativas = 5

print('''\n\033[40;1m O computador sorteou um número de 1 a 100. Será que você consegue advinhar qual é?  \033[m
\033[40;1m (Você só tem 5 tentativas!) \033[m''')

while tentativas > 0:
    escolha = str(input('\nTente acertar: ')).strip().replace(" ", "")

    if not escolha.isnumeric():
        print('\033[31mDigite apenas números!\033[m')
        continue

    escolha = int(escolha)

    if escolha > 100 or escolha < 1:
        print('\033[31mNúmero fora do intervalo (1 a 100)!\033[m')
        continue

    tentativas -= 1

    if escolha == numeroescolhido:
        print(f'''\nParabéns! {numeroescolhido} foi o número sorteado!
        Você ganhou!''')
        break
    elif tentativas <= 0:
        print(f'\n\033[1mVocê excedeu o número de tentativas!\033[m\n\033[31mGame Over!\033[m')
        print(f'O número correto era \033[32m{numeroescolhido}\033[m.')
        break
    elif escolha > numeroescolhido:
        print(f'\n\033[31;1mVocê errou!\033[m \033[1mO número sorteado é menor que {escolha}!\033[m\n\033[40;1m (Você tem {tentativas} tentativa!) \033[m\n')
    elif escolha < numeroescolhido:
        print(f'\n\033[31;1mVocê errou!\033[m \033[1mO número sorteado é maior que {escolha}!\033[m\n\033[40;1m (Você tem {tentativas} tentativa!) \033[m\n')
