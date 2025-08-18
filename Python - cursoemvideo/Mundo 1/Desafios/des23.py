n1 = str(input("Digite um número: "))
n1 = n1.strip()
n1 = n1.zfill(4)
print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}""".format(n1[3], n1[2], n1[1], n1[0]))