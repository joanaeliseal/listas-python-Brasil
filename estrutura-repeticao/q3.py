# Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = str(input("Digite seu nome: "))
while (len(nome) <= 3):
    print("Nome inválido!")
    nome = str(input("Digite novamente: "))
    
idade = int(input("Digite sua idade: "))
while (idade <= 0) or (idade > 150):
    print('Idade inválida')
    idade = int(input("Digite novamente: "))

salario = float(input("Digite seu salário: "))
while (salario > 0.0):
    print("inválido!")
    salario = float(input("Digite seu salário: "))
else:
  salario == True

sexo = str(input("Digite seu sexo (f ou m): "))
while sexo == 'f' or sexo == 'm':
    sexo = str(input("Digite seu sexo: "))
else:
    sexo == False

estado = str(input("Digite seu estado civil: "))
while estado != ['s, c, v, d']:
    print('Estado civil inválido. Tente novamente!')
    estado = str(input("Digite seu estado civil: "))