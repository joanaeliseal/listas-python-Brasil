# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
# mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str(input("Digite o nome de usuário: "))
senha = str(input("Digite sua senha: "))

while nome == senha:
    print('A senha não pode ser igual ao nome de usuário! Tente novamente.')
    senha = str(input('Digite outra senha: '))
    
