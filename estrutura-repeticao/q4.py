# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e 
# que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. 
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou 
# iguale a população do país B, mantidas as taxas de crescimento.

paisA = 80000
A = 0.03
paisB = 200000
B =  0.015
anos = 0

populacao_a = paisA * A
populacao_b = paisB * B

while populacao_a < populacao_b:
    populacao_a *= A
    populacao_b *= B
    anos += 1
else:
    print("população de A: {populacao_a:.2f}")
    print("população de B: {populacao_b:.2f}")
    print(anos, " anos")