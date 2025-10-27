primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
contador = 0

print(f'{primeirotermo}', end=' -> ')

while contador != 9:
    contador += 1
    primeirotermo += razao
    print(f'{primeirotermo}', end=' -> ')

print('FIM')