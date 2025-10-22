frase = str(input('Digite uma frase: '))
frase = frase.replace(' ', '').strip().lower()
fraseinv = ''

for letra in range(len(frase) -1, -1, -1):
    fraseinv += frase[letra]
if frase == fraseinv:
    print(f'{frase} é um políndromo!')
else:
    print(f'Não é um políndromo!')
