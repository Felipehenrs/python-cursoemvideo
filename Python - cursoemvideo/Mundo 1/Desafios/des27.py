nome = str(input("Digite seu nome: "))
nome = nome.title()
print('Seu primeiro nome é {} e o último {}.'.format(nome.split()[0], nome.split()[-1]))