# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# F - 32/9 = C *5
# F / 9 = C*5*32
# F = (C*32)*1,8

C = float(input('Digite a temperatura em Celsius: '))

F = (C*1.8)+32

print(f'A temperatura em Fahrenheit é: {F:.2f} graus')