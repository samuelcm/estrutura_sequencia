#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
#em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
#é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
#que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

area= float(input("Bem vindo a nossa loja!\n Quantos metros quadrados possui área da parede a ser pintada?\n"))
tamanho_lata = 18
lata = 3*tamanho_lata
qtd_lata = area / lata
lata_arredondado = math.ceil(qtd_lata)

if lata_arredondado == 1:
    print("Você precisará de {0} lata.".format(lata_arredondado))
else:
    print("Você precisará de {0} latas.".format(lata_arredondado))
