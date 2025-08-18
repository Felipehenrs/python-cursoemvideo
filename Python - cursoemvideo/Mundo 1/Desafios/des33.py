# n1 = int(input('Digite um número: '))
# n2 = int(input('Digite o segundo número: '))
# n3 = int(input('Digite o terceiro número: '))
# if n1 < n3 < n2:
#     print("O maior número é {}, e o menor número é {}.".format(n2, n1))
# elif n1 < n2 < n3:
#     print('O maior número é {}, e o menor número é {}.'.format(n3, n1))
# elif n2 < n3 < n1:
#     print('O maior número é {}, e o menor número é {}.'.format(n1, n2))
# elif n3 < n2 < n1:
#     print('O maior número é {}, e o menor número é {}.'.format(n1, n3))
# elif n2 < n1 < n3:
#     print('O maior número é {}, e o menor número é {}.'.format(n3, n2))
# elif n3 < n1 < n2:
#     print('O maior número é {}, e o menor número é {}.'.format(n2, n3))



#Código chat
n1 = int(input('Digite um número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O maior número é {}, e o menor número é {}.'.format(maior, menor))
