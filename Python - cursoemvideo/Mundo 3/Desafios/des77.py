palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
    vogaltem = ''

    for letra in palavra:

      if letra in vogais:
        vogaltem += letra+' '

    print(f'Na palavra {palavra.upper()} temos {vogaltem}')