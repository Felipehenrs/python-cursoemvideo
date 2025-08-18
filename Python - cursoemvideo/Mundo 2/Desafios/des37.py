n1 = int(input('Digite um número decimal: '))
conve = int(input('Digite "1" para binário, "2" para octal e "3" para hexadecimal: '))
if conve == 1:
    print('O número {} convertido para binário é "{:b}".'.format(n1, n1))
elif conve == 2:
    print('O número {} convertido para octal é "{:o}".'.format(n1, n1))
elif conve == 3:
    print('O número {} convertido para hexadecimal é "{:X}".'.format(n1, n1))



