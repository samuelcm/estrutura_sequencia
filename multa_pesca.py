#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
#(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
#variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
#e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

pesca= input("Quantos quilos você pescou hoje?")
pesca = float(pesca)
limite_kg = 50.
kg_exc = pesca - limite_kg
multa = float(4.0 * kg_exc)


if pesca<limite_kg:
    print("não há excedente nem multa para pagar")
else:
    print("Excedente de {0} quilos. Você deverá pagar R$ {1} reais de multa.".format(kg_exc,multa))
