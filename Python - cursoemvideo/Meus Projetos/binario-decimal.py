from math import trunc
n0 = int(input("numero: "))
n1 = n0%2
n1a = trunc(n0/2)
n2 = n1a%2
n2a = trunc(n1a/2)
n3 = n2a%2
n3a = trunc(n2a/2)
n4 = n3a%2
n4a = trunc(n3a/2)
n5 = n4a%2
n5a = trunc(n4a/2)
n6 = n5a%2
n6a = trunc(n5a/2)
n7 = n6a%2
n7a = trunc(n6a/2)
n8 = n7a%2
n8a = trunc(n7a/2)
print("Binário: {}{}{}{}{}{}{}{}".format(n8, n7, n6, n5, n4, n3, n2, n1))
print("Quociente: {}, {}, {}, {}, {}, {}, {}, {}".format( n1a, n2a, n3a, n4a, n5a, n6a, n7a, n8a))