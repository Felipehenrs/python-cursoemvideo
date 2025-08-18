fra = str(input("Digite uma frase: "))
fra = fra.strip().lower()
print('''A letra "A" aparece {} na frase {}.
"A" está localizado pela primeira vez no dígito {}.
"A" apareceu pela última vez no dígito {}.'''.format(fra.count("a")
                                                        , fra, fra.find("a"), fra.rfind("a")))