print('\033[40;1mSUPER PROGRESSÃO ARITMÉTICA!\033[m\n')

primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 0

print(f'{primeirotermo}', end=' -> ')

while True:

    while contador != 9:
        contador += 1
        primeirotermo += razao
        print(f'{primeirotermo}', end=' -> ')

    print('PAUSE')

    segundachance = int(input('Quantos termos quer mostrar a mais? '))
    contador -= segundachance
    if segundachance == 0:
        print('FIM DO PROGRAMA')
        break
