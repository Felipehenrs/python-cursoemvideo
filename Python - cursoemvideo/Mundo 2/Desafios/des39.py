from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
if idade <= 17:
    print('Você tem {} anos! Ainda não precisa se alistar, faltam {} anos para que precise.'.format(idade, 18 - idade))
elif idade >= 19:
    res = str(input('Você tem {} anos! Já passou {} anos da data de alistamento. Já se alistou? (Use "y" para SIM e "n" para NÂO): '.format(idade, idade - 18)))
    if res == 'y':
        print('Você é um ótimo cidadão!')
    elif res == 'n':
        print('Você precisa se alistar o mais rápido possível!')
else:
    print('Você tem 18 anos! está na idade para se alistar!😁')
