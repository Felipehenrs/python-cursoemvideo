print('\033[40;1m MERCADINHO ARAÚJO \033[m')

precottl = mil = precomenor = nomemenor = 0

while True:
    nomeproduto = str(input('\nDigite o nome do produto: '))
    preco = float(input('Preço: R$'))
    precottl += preco

    if precomenor == 0.0:
        precomenor = preco
        nomemenor = nomeproduto
    if  preco < precomenor:
        precomenor = preco
        nomemenor = nomeproduto


    if preco < 0:
        print('Digite o preço correto!')
    if preco > 1000:
        mil += 1

    continuar = str(input('\nDeseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue
print(f'''\nO total da compra foi R${precottl:.2f}
Temos {mil} produtos custando mais de R$1000.00
O produto mais barato foi {nomemenor} que custa R${precomenor:.2f}''')


