tupla = ()
contar = 0

for v in range(1, 5):
    n1 = int(input(f'Digite o {v}º número: '))
    tupla += (n1,)

print(f'\nVocê digitou os valores {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3) + 1}ª posição')
else:
    print(f'O número 3 não aparece nessa tupla')

for valor in tupla:
    if valor % 2 == 0:
        contar += 1

print(f'Os valores pares digitados foram {contar}')