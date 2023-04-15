# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanho_m_quadrado_parede = float(input('Digite o tamanho em metros quadrados da área a ser pintada: '))
cobertura_da_tinta_1_litro = ((tamanho_m_quadrado_parede)/3)
capacidade_pintura = 18
preco = 80.0

latas = cobertura_da_tinta_1_litro/capacidade_pintura

totall = latas * preco

print(f' Você usará {latas:.2f} lata(s) de tinta')
print(f' O preco total é de: R$ {totall:.2f}')