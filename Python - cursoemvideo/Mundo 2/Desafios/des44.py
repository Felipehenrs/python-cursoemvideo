print('\033[1:40mPROGRANA PARA VER JUROS/DESCONTOS A SER PAGO EM CIMA DE UM PRODUTO\033[m')

valor = float(input('\033[1mQual o valor do produto? (Sem pontos e vírgulas): \033[mR$'))
forma = int(input('''\033[1mQual a forma de pagamento?\033[m
 (Digite "\033[1:32m1\033[m" para à vista no dinheiro/cheque)
 (Digite "\033[1:34m2\033[m" para à vista no cartão)
 (Digite "\033[1:31m3\033[m" para até 2x no cartão)
 (Digite "\033[1:35m4\033[m" para 3x ou mais no cartão)
 \033[1mDigite:\033[m '''))

if forma == 1:
    print('Nessa forma de pagamento você ganha \033[1:36m10%\033[m '
          'de desconto. O total a pagar é de \033[1mR${:.2f}\033[m .'.format(valor - ((valor / 100) * 10)))
elif forma == 2:
    print('Nessa forma de pagamento você ganha \033[1:36m5%\033[m '
          'de desconto. O total a pagar é de \033[1mR${:.2f}\033[m .'.format(valor - ((valor / 100) * 5)))
elif forma == 3:
    print('Nessa forma de pagamento o valor não sofre alterações.'
          ' O valor de suas prestações mensais será \033[1mR${:.2f}p/mês\033[m, totalizando \033[1mR${:.2f}\033[m .'.format(valor / 2, valor))
elif forma == 4:
    quant = int(input('\033[1mDe quantas vezes você que pacelar?\033[m '))
    print('Nessa forma de pagamento cobramos \033[1:36m20%\033[m de juros.'
          ' O valor de suas prestações mensais será \033[1mR${:.2f}p/mês\033[m, totalizando \033[1mR${:.2f}\033[m .'
          .format((valor + ((valor / 100) * 20)) / quant, valor + ((valor / 100) * 20)))