lar = float(input("Qual a largura da parede (em metros)?" ))
alt = float(input("Qual a altura da parede (em metros)?" ))
print("A largura do seu muro é {}m, e a altura é {}m.".format(lar, alt))
print("A área dessa parede é {:.2f}m² e vai precisar de {:.2f}l .".format(lar * alt, (lar * alt) /2))
