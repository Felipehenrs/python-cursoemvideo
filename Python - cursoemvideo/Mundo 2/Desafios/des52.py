n1 = int(input('Digite um número: '))

total = 0

for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
if total == 2:
    print(f'\n\033[mEsse número é primo!\n')
else:
    print('\n\033[mEsse número não é primo!\n')


