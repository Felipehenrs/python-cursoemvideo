from datetime import date
print('\033[7:40m---CONFEDERAÇÃO NACIONAL DE NATAÇÃO---\033[m')
ano = int(input('Para saber sua categoria, diga, qual o ano que você nasceu? '))
idade = date.today().year - ano
if idade > 120 or idade < 0:
    print('\033[31mEssa não é sua data de nascimento!\033[m')
else:
    if idade <= 9:
        print('\033[1:40mMIRIM\033[m')
    elif idade <= 14:
        print('\033[1:47mINFANTIL\033[m')
    elif idade <= 19:
        print('\033[1:44mJUNIOR\033[m')
    elif idade <= 23:
        print('\033[1:46mSÊNIOR\033[m')
    else:
        print('\033[1:41mMASTER\033[m')
