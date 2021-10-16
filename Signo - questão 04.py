def signo(d, m):
    if d >= 21 and m == 3 or d <= 19 and m == 4:
        print('Áries')
    elif d >= 20 and m == 4 or d <= 20 and m == 5:
        print('Touro')
    elif d >= 21 and m == 5 or d <= 21 and m == 6:
        print('Gêmeos')
    elif d >= 22 and m == 6 or d <= 22 and m == 7:
        print('Câncer')
    elif d >= 23 and m == 7 or d <= 22 and m == 8:
        print('Leão')
    elif d >= 23 and m == 8 or d <= 22 and m == 9:
        print('Virgem')
    elif d >= 23 and m == 9 or d <= 22 and m == 10:
        print('Libra')
    elif d >= 23 and m == 10 or d <= 21 and m == 11:
        print('Escorpião')
    elif d >= 22 and m == 11 or d <= 21 and m == 12:
        print('Sagitário')
    elif d >= 22 and m == 12 or d <= 19 and m == 1:
        print('Capricórnio')
    elif d >= 20 and m == 1 or d <= 18 and m == 2:
        print('Aquário')
    elif d >= 19 and m == 2 or d <= 20 and m == 3:
        print('Peixes')

dia = int(input('Dia de nascimento: '))
mes = int(input('Mês de nascimento: '))
signo(dia, mes)

