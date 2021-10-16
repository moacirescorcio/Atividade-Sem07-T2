from typing import Counter


nome = input('Insira seu nome: ').strip()
estado_civil = input('Qual seu estado civil? 1 - Casado 2 - Solteiro').strip()
num_carac= len(nome)

if estado_civil == '1':
    nome_conjuge = input('Qual o nome do cônjuge? ').strip()
    num_carac2 = len(nome_conjuge)
    resultado = num_carac + num_carac2
    print(resultado)
elif estado_civil == '2':
    print(num_carac)
else:
    print()