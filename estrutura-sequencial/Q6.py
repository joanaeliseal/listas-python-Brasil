# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from cmath import pi

r = float(input('Digite o raio: '))
A = pi*(r**2)

print(f'A área do círculo é: {A:.2f}')