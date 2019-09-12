#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

contagem = 0
total_nota=0
ordem_nota = 1
while contagem <4:
    print("Digite a nota", ordem_nota)
    nota = int(input(" "))
    total_nota = total_nota + nota
    contagem = contagem +1
    ordem_nota = ordem_nota +1

media = total_nota/contagem

print ("A media é", media)
