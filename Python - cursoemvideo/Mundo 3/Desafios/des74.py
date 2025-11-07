from random import randint

numeros = tuple(randint(1, 100) for _ in range(5))

print(f'Os números sorteados foram {numeros}')

menor = maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
    elif numero <= menor:
        menor = numero

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')