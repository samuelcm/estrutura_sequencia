#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

contagem = 1

while contagem <= 1:
    num1 = input("digite um numero inteiro\n")
    try:
        num1 = int(num1)
    except:
        print ("digite um numero valido")
        continue

    num2 = input("digite um numero inteiro\n")
    try:
        num2 = int(num2)
    except:
        print ("digite um numero valido")
        continue
    contagem += 1

cont = 1
while cont <= 1:
    num3 = input("digite um numero real\n")
    try:
        num3 = float(num3)
    except:
        print ("digite um numero valido")
        continue
    cont += 1
soma = 3*num1 + num3
produto = (num1*2) * (num2/2)
cubo = num3**3
print(produto, soma, cubo)



#int1 = int(int1)
