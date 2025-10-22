from datetime import date

atual = date.today().year
maior = 0
menor = 0

for i in range(1, 7 + 1):
    idade = int(input(f'Digite em que ano a {i}º pessoa nasceu: '))
    if (atual - idade) >= 18:
        maior += 1
    elif (atual - idade) < 18:
        menor += 1
print(f'\nDessas {i} pessoas, {maior} são maiores de idade e {menor} são menores de idade.')


