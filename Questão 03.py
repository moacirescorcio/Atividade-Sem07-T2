def eh_impar(n):
    if n <= 9 or n >= 100:
        return
    else:
        u = n % 10
        n = n // 10
        d = n % 10
        if u % 2 != 0 and d % 2 !=0:
            print('Os dois dígitos são ímpares.')
        elif u % 2 != 0 or d % 2 != 0:
            print('Apenas um dígito é ímpar.')
        else:
            print('Nenhum dígito é ímpar.')

numero = int(input('Insira um número entre 10 e 99: '))
eh_impar(numero) 