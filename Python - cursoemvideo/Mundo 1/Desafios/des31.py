dis = float(input('Qual a distância dessa viagem?'))
if dis <= 200:
    print('O valor da sua viagem de {}Km será R${:.2f} com base nos R$0.50 por km.'.format(dis, 0.5 * dis))
else:
    print('O valor da sua viagem de {}Km será R${:.2f} com base nos R$0.45 por km.'.format(dis, 0.45 * dis))
print('''
A taxa para viagens até 200km será de R$0.50 por km, acima disso a taxa será R$0.45Km.''')