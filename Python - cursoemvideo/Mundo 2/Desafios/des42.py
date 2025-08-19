print('\033[40mTriãngulo equilátero, isósceles ou escaleno.\033[m')
la1 = float(input('Digite o valor do primeiro lado: '))
la2 = float(input('Digite o valor do segundo lado: '))
la3 = float(input('Digite o valor do terceiro lado: '))
if la1 + la2 > la3 and la1 + la3 > la2 and la3 + la2 > la1:
    if la1 == la2 == la3:
        print('\033[1:43mEQUILÁTERO!\033[m')
    elif la1 == la2 or la1 == la3 or la3 == la2:
        print('\033[1:42mISÓSCELES!\033[m')
    else:
        print('\033[1:41mESCALENO!\033[m')
else:
    print('\033[31mIsso não pode formar um triângulo!\033[m')
