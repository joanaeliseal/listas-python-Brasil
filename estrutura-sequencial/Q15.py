# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
#Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#   salário bruto. 
#   quanto pagou ao INSS.
#   quanto pagou ao sindicato.
#   o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
#       + Salário Bruto : R$
#       - IR (11%) : R$
#       - INSS (8%) : R$
#       - Sindicato ( 5%) : R$
#       = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

ganho_hora1 = float(input('Quando você ganha por hora: '))
numero_hora1 = int(input('Qual o número de horas trabalhadas no mês: '))
salario_bruto = ganho_hora1*numero_hora1
IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
Sindicato = salario_bruto * 0.05
desconto = IR + INSS + Sindicato
salario_liquido = salario_bruto - desconto

print(f'No mês o salário bruto é de R$ {salario_bruto:.2f}')
print(f'O desconto do mês de IR R$ {IR:.2f}, INSS R$ {INSS:.2f} e Sindicato R$ {Sindicato:.2f} no qual o total descontado foi de R${desconto}')
print(f'No mês o salário líquido é de R$ {salario_liquido:.2f}')