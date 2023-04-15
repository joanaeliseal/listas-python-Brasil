# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
# Vida de TO lascada!!!

valor_hora = float(input('Digite o quanto você ganha por hora: '))
hora_trabalho = float(input('Digite o número de horas trabalhadas no mês: '))
total_salario = valor_hora*hora_trabalho

print(f'Seu salário mensal de TO lascada era de R$: {total_salario:.2f}')
