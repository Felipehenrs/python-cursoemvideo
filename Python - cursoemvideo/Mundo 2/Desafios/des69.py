print('\033[40;1m CADASTRE UMA PESSOA \033[m')

idadeacumular = menina = homem = 0

while True:

    idade = int(input('\nIdade: '))
    if idade >= 18:
        idadeacumular += 1

    sexo = str(input('Sexo: [F/M] ')).strip().upper()
    if sexo == 'F' and idade < 20:
        menina += 1
    elif sexo == 'M':
        homem += 1

    print('\nArmazenando os dados...\n')

    continuar = str(input('\nDeseja continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue
print(f'''\nTotal de pessoas com mais de 18 anos: {idadeacumular}
Ao todo temos {homem} homens cadastrados
E temos {menina} mulheres menores de 20 anos''')