from random import randint
com = randint(1, 5)
user = int(input("Tente advinhar qual o número que o computador irá escolher entre 1 e 5: "))
if user == com:
    print("Parabéns! Você acertou!")
else:
    print("Que pena! Você errou. A resposta certa era {}.".format(com))