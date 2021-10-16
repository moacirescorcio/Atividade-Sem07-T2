def ordem(n1, n2, n3):
    if n1 < n2 < n3:
        print(f'Em ordem crescente: {n1}, {n2}, {n3}')
    elif n1 < n3 < n2:
        print(f'Em ordem crescente:{n1}, {n3}, {n1}')
    elif n2 < n1 < n3:
        print(f'Em ordem crescente:{n2}, {n1}, {n3}')
    elif n2 < n3 < n1:
        print(f'Em ordem crescente:{n2}, {n3}, {n1}')
    elif n3 < n1 < n2:
        print(f'Em ordem crescente:{n3}, {n1}, {n2}')
    elif n3 < n2 < n1:
        print(f'Em ordem crescente:{n3}, {n2}, {n1}')

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))
ordem(n1, n2, n3)