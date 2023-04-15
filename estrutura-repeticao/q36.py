# Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada 
# não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário

n_tabuada = int(input("\nDigite o número para fazer a tabuada: "))
n_inicial = int(input("Iniciar a tabuada no : "))
n_final = int(input("Finalizar a tabuada no : "))

caminho = n_inicial

for i in range(n_inicial, n_final + 1):
    print(n_tabuada, " X ", caminho, " = ", n_tabuada * caminho)
    caminho += 1