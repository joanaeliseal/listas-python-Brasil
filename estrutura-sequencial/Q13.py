# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura_2 = float(input('Digite a altura: '))
peso_homem = (72.7*altura_2) - 58
peso_mulher = (62.1*altura_2) - 44.7
print(f'O peso ideal para o homem é: {peso_homem:.2f}') 
print(f'O peso ideal para a mulher é: {peso_mulher:.2f}') 
