n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
if n1 > 10.0 or n1 < 0 or n2 > 10.0 or n2 < 0 or n3 > 10.0 or n3 < 0:
    print('\n\033[1:31mNotas variam de 0 a 10!!!')
else:
    if media <= 5.0:
        print(f'\nSua média foi {media:.2f}\n \033[31mREPROVADO!')
    elif media <= 6.9:
        print(f'\nSua média foi {media:.2f}\n \033[33mRECUPERAÇÃO!')
    else:
        print(f'\nSua média foi {media:.2f}\n \033[32mAPROVADO!')