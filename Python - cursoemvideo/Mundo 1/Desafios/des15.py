quantdias = float(input("Quantos dias você alugou o carro? "))
quantkm = float(input("Quantos km você rodou com o carro? "))
print("O preço a pagar por um dia de aluguel é R$60,00. O preço a pagar por km rodado é R$0.15. Sabendo que "
      "você alugou {} dias e rodou {}km, o total a pagar é R${}.".format(quantdias, quantkm, quantdias * 60 + quantkm * 0.15))

