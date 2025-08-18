nome = str(input("Qual o seu nome completo? "))
print("""O seu nome com letras maiúsculas é esse {}. 
Com as letras minúsculas é esse {}.
Tem {} letras ao todo, sem considerar os espaços.
O primeiro nome tem {} letras.""".format(nome.upper(), nome.lower(),
                                         len(nome.replace(" ", "")),
                                         len(nome.split()[0])))