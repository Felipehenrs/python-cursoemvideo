tupla = ('Lápis', '1.50', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Compasso', '9.99', 'Transferidor', '4.20', 'Mochila', '120.32', 'Canetas', '22.30', 'Livro', '34.90')
x = 0

print('-'*40)
print('          LISTAGEM DE PREÇOS')
print('-'*40)

for item in tupla:
    if x % 2 == 0:
        print(f'{item.ljust(30, '.')}'f'R$ {tupla[x+1]}')
    x += 1
print('-'*40)

