print('\033[40mTABUADA 2.0\033[m')
n1 = str(input('Digite um número para saber sua tabuada: '))
n1 = n1.strip()
if n1.isdigit():
    n1 = int(n1)
    for f in range(0, 10+1):
        print(f'{n1} x {f} = {n1 * f}')
    print('\n\033[1mQuer multiplicar por um número específico?\033[m (\033[32m"1"SIM\033[m   \033[31m"2"NÃO\033[m)')
    exclusivo = str(input('Resposta: '))
    exclusivo = exclusivo.strip()
    if exclusivo.isdigit():
        exclusivo = int(exclusivo)
        if exclusivo == 1:
            n2 = int(input('Digite por quanto que quer multiplicar: '))
            print(f'{n1} x {n2} = {n1 * n2}')
            print('FIM')
        elif exclusivo == 2:
            print('FIM')
        elif exclusivo != 1 or exclusivo != 2:
            print('\033[31mDIGITE UMA DAS ALTERNATIVAS!!!\033[m')
    else:
        print('\033[31mDIGITE UMA DAS ALTERNATIVAS!!!\033[m')
else:
    print('\033[31mDIGITE UM NÚMERO INTEIRO!!!\033[m')

