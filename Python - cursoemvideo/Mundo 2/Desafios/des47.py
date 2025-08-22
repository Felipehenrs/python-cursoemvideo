from time import sleep
print('\n\033[1:40mEsses são todos os número pares de 0 a 50:\033[m\n')
for par in range(0, 51, 2):
    sleep(0.05)
    print(par, end=' ')
print('\n\033[1:40mEsses são todos os número ínpares de 0 a 50:\033[m\n')
for impar in range(1, 51, 2):
    sleep(0.05)
    print(impar, end=' ')
