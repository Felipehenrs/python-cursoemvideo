while True:
    n1 = int(input('\nQuer ver a tabuáda de qual valor? '))
    print('-'*30)

    if n1 >= 0:
        for c in range(1, 11):
            print(f'{n1} x {c} = {n1*c}')
    else:
        break