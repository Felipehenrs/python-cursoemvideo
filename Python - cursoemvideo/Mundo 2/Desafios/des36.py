valorcasa = float(input('Qual o valor da casa que você quer comprar? '))
salario = float(input('Diga quanto você ganha: '))
anos = float(input('Em quantos anos deseja pagar: '))
exceder = (salario / 100) * 30
prestacao = valorcasa / (anos * 12)
if prestacao <= exceder:
    print(f'O valor que você pagará por mês de prestação será R${prestacao:.2f} .')
else:
    print('Lamento! seu salário não é o nescessário para o empréstimo.')

