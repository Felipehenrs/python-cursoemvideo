import math
o = float(input("Comprimento do cateto oposto: "))
a = float(input("Comprimento do cateto adjacente: "))
h = a ** 2 + o ** 2
print("A hipotenusa vai medir {:.2f}".format( math.sqrt(h)))

h = math.hypot(o, a)
print("A hipotenusa vai medir {:.2f}".format( h))
