print('\033[40mVEJA O STATUS DE PESO REFERENTE AO SEU IMC.\033[m')
peso = str(input('Qual seu peso: Kg'))
altura = str(input('Qual sua altura? m'))

if '.' in altura:
    altura = float(altura)
    peso = float(peso)
    imc = peso / (altura * altura)
else:
    altura = float(altura)
    peso = float(peso)
    if altura <= 0:
        altura = float(altura)
    else:
        imc = peso / ((altura / 100) * (altura / 100))

if altura <= 0 or peso <= 0:
    print('\033[31mDIGITE SEU PESO/ALTURA VERDADADEIRO!\033[m')
else:
    if imc <= 18.5:
        print(f'Seu IMC é {imc:.2f}Kg/m². \033[1:47mVOCÊ ESTÁ ABAIXO DO PESO!\033[m')
    elif imc <= 25:
        print(f'Seu IMC é {imc:.2f}Kg/m². \033[1:44mVOCÊ ESTÁ NO PESO IDEAL!\033[m')
    elif imc <= 30:
        print(f'Seu IMC é {imc:.2f}Kg/m². \033[1:42mVOCÊ ESTÁ COM SOBREPESO!\033[m')
    elif imc <= 40:
        print(f'Seu IMC é {imc:.2f}Kg/m². \033[1:43mVOCÊ ESTÁ COM OBESIDADE!!\033[m')
    else:
        print(f'Seu IMC é {imc:.2f}Kg/m². \033[1:41mVOCÊ ESTÁ COM OBESIDADE MÓRBIDA!!!\033[m')




















