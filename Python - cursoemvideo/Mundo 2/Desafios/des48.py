print('\033[40mPROGRAMA QUE CALCULA NUMEROS ÍMPARES MULTIPLOS DE 3!\033[m')
s = 0
for f in range(3, 501, 3):
    if f % 2 != 0:
        s += f
print(f'A soma entre os números ímpares multiplos de \033[34m3\033[m é \033[1m{s}\033[m!')