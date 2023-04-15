# Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input('Digite uma nota: '))

while nota >=0 and nota <= 10:
    print('Valor válido!')
    nota += 1

if nota<0 or nota>10:
    print('Valor inválido')
    nota = int(input('Não pode ser menor que 0 nem maior que 10!\n Tente novamente.'))
