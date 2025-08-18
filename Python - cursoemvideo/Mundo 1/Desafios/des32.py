# ano = int(input('Quer saber se esse ano é bissexto? '))
# if ano % 4 == 0:
#     if ano % 100 != 0:
#         print('ESSE NÚMERO É BISSEXTO!!!')
#     else:
#         if ano % 400 == 0:
#             print('ESSE NÚMERO É BISSEXTO!!!')
#         else:
#             print('Isso é só um ano normal.')
# else:
#     print('Isso é só um ano normal.')








ano = int(input('Quer saber se esse ano é bissexto? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('ESSE ANO É BISSEXTO!!!')
else:
    print('É só um ano comum.')