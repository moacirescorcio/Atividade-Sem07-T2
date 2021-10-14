from typing import Counter


nome = input()
estado_civil = input()
num_carac= len(nome)

if estado_civil == '1':
    nome_conjuge = input()
    num_carac2 = len(nome_conjuge)
    resultado = num_carac + num_carac2
    print(resultado)
elif estado_civil == '2':
    print(num_carac)
else:
    print()