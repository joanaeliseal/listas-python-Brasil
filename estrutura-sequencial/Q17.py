#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

tamanho_m_quadrado_parede = float(input('Digite o tamanho em metros quadrados da área a ser pintada: '))
cobertura_da_tinta_1_litro = ((tamanho_m_quadrado_parede)/6)
capacidade_pintura_lata = 18
capacidade_pintura_galao = 3.6
preco_lata = 80.0
preco_galao = 25.0

latas = cobertura_da_tinta_1_litro/capacidade_pintura_lata
galoes = cobertura_da_tinta_1_litro/capacidade_pintura_galao

totallata = latas * preco_lata
totalgalao = latas * preco_galao

lata_grande = latas
lata_pequena = (cobertura_da_tinta_1_litro -(lata_grande*180))/21.6

print(f' Você usará {latas:.2f} lata(s) de tinta')
print(f' O preco total é de: R$ {totallata:.2f}')

print(f' Você usará {galoes:.2f} lata(s) de tinta')
print(f' O preco total é de: R$ {totalgalao:.2f}')

print(f' Latas Grandes {lata_grande:.0f} e latas pequenas {lata_pequena:.0f} ')