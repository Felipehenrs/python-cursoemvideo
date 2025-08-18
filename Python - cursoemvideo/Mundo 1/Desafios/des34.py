salario = float(input('Qual o seu salário? R$'))
quinze = (salario / 100) * 15
dez = (salario / 100) * 10
if salario <= 1250:
    print('Seu salário com 15% de aumento é R${:.2f} .'.format(salario + quinze))
else:
    print('Seu salário com 10% de aumento é R${:.2f} .'.format(salario + dez))
