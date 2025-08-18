import math
ang = float(input("Digite o ângulo que você deseja: "))
ang1 = math.radians(ang)
print("O ângulo de {} tem o SENO de {:.2f}"
      "\nO ângulo de {} tem o COSSENO de {:.2f}"
      "\nO ângulo de {} tem a TANGENTE de {:.2f}".format(ang, math.sin(ang1), ang,
                                                   math.cos(ang1), ang, math.tan(ang1)))