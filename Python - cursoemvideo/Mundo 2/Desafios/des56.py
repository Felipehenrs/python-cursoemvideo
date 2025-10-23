mediaidade = 0
idadehomens = 0
mulheresmaisnovas = 0

for quantidade_pessoas in range (1, 5):
    pessoa = str(input(f'Digite o nome da {quantidade_pessoas} pessoa: '))
    idade = int(input(f'Digite a idade dessa pessoa: '))
    sexo = int(input(f'Digite o sexo dessa pessoa. (Digite "1" para masculino e "2" para feminino) -> '))
    mediaidade += idade
    if sexo == 1 and idade >= idadehomens:
        idadehomens = idade
        maisvelho = pessoa
    elif sexo == 2 and idade < 20:
        mulheresmaisnovas += 1

print(f'A média da idade do grupo é {mediaidade / 4}, o nome do homem mais velho é {maisvelho} e a '
      f'quantidade de mulheres mais novas que 20 anos é {mulheresmaisnovas}.')