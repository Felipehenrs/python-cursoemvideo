while True:
    escolha = 1
    n1 = float(input('\nDigite o 1º número: '))
    n2 = float(input('Digite o 2º número: '))

    while escolha != 4:
        escolha = str(input(''' 
    (Digite "1" para somar)
    (Digite "2" para multiplicar)
    (Digite "3" para saber o maior)
    (Digite "4" para escolher novos números)
    \033[1;31m(Digite "0" para sair)\033[m
    Escolha: ''')).replace(" ", "")

        if escolha in ["1", "2", "3", "4", "0"] and escolha.isnumeric():
            escolha = int(escolha)

            if escolha == 1:
                print(f'\n\033[32mA soma entre {n1} e {n2} = {n1 + n2}\033[m')

            elif escolha == 2:
                print(f'\n\033[36mA multiplicação entre {n1} e {n2} = {n1 * n2}\033[m')

            elif escolha == 3:
                if n1 > n2:
                    print(f'\n\033[33mO maior número entre {n1} e {n2} = {n1}\033[m')
                elif n1 == n2:
                    print('\n\033[34mOs dois números têm o mesmo valor!\033[m')
                else:
                    print(f'\n\033[33mO maior número entre {n1} e {n2} = {n2}\033[m')

            elif escolha == 4:
                break

            elif escolha == 0:
                print('\n\033[31mEncerrando o programa...\033[m')
                exit()

            print('==-==-==-==-==-==-==-==-==-==-==-==-==-==')

        else:
            print('\n\033[31;1mDigite um valor válido!\033[m')
