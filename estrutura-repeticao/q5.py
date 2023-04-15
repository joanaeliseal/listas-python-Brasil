# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
# Valide a entrada e permita repetir a operação.

popPais_A = int(input("pais A: "))
cresAnual_A = float(input("porcentagem de crescimento A: "))
popPais_B = int(input("país B: "))
cresAnual_B = float(input("porcentagem de crescimento B: "))

anos = 0

porcentagem_A = (1 + (cresAnual_A / 100))
porcentagem_B = (1 + (cresAnual_B / 100))

popAtual_a = popPais_A * porcentagem_A
popAtual_b = popPais_B * porcentagem_B

while popAtual_a < popAtual_b:
  popAtual_a *= porcentagem_A
  popAtual_b *= porcentagem_B
  anos += 1
else:
  print("população de A: %.2f" %popAtual_a)
  print("população de B: %.2f" %popAtual_b)
  print(anos, " anos")