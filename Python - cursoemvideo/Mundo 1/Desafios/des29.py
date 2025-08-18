km = float(input('Qual a velocidade do carro? '))
multa = (km - 80) * 7
if km <= 80:
    print('Essa velocidade é permitida.')
else:
    print('Está acima do limite permitido. Você recebeu uma multa de R${:.2f} .'.format(multa))