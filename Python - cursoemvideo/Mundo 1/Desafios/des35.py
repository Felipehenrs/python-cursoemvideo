la1 = float(input('Fale o valor do primeiro lado: '))
la2 = float(input('Fale o valor do segundo lado: '))
la3 = float(input(('Fale o valor do terceiro lado: ')))
if la1 + la2 > la3 and la1 + la3 > la2 and la2 + la3 > la1:
    print('Os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('Os segmentos acima não podem formar um triângulo')