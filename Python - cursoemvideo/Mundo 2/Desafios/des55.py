peso = float(input('Qual o peso da 1ª pessoa? '))
maior = peso
menor = peso

for i in range(2, 5 + 1):
    peso = float(input(f'Qual o peso da {i}º pessoa? '))
    if peso >= maior:
        maior = peso
    elif peso < maior and peso < menor:
        menor = peso
print(f'O maior peso é {maior} e o menor peso é {menor}.')