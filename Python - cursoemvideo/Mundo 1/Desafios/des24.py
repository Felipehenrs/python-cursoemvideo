nc = str(input("Nome da cidade: "))
nc = nc.title()
nc1 = nc.split()[0]
print("Santo é o primeiro nome da cidade {}? {}".format(nc, "Santo" in nc1))