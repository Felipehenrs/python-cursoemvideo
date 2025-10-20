print('\033[1;40mPROGRESSÃO ARITMÉTICA!\033[m\n')

ax = int(input('Primeiro termo: '))
razao = int(input('Rasão: '))
decimo = ax + (11 - 1) * razao

for c in range(ax, decimo, razao):
    print(c, end=' --> ')
print('END')