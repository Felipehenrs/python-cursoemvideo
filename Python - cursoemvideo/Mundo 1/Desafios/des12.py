preco = float(input("Qual o preço do produto (Em Reais)?" ))
descon = int(input("Qual o valor do desconto (Em porcentagem)? "))
descontotal = (descon / 100) * preco
print("Adicionando {}% de desconto á esse produto de R${}, o valor será R${}.".format(descon, preco, preco - descontotal))