def e_par(numero):
    if numero <= 99 or numero >= 1000:
        return
    else:
        u = numero % 10
        numero = numero // 10
        d = numero % 10
        numero = numero // 10
        c = numero % 10
        if u % 2 == 0 and d % 2 == 0 and c % 2 == 0:
            print('Tem 3 dígitos pares!')
        elif u % 2 == 0 and d % 2 == 0:
            print('Tem 2 dígitos pares!')
        elif u % 2 == 0 and c % 2 == 0:
            print('Tem 2 dígitos pares!')
        elif d % 2 == 0 and c % 2 == 0:
            print('Tem 2 dígitos pares!')
        elif c % 2 == 0:
            print('Tem 1 dígito par!')
        elif d % 2 == 0:
            print('Tem 1 dígito par!')
        elif u % 2 == 0:
            print('Tem 1 dígito par!')
        else:
            print('Não há números pares!')
          

numero = int(input('Insira um número entre 100 e 999: '))
e_par(numero)
