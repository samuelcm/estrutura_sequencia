#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1 = int(input("digite um numero inteiro\n"))
n2 = int(input("digite outro numero inteiro\n"))
n3 = float(input("digite um numero real\n"))

r1 = (n1**2)*(n1/2)
r2 = (n1*3) + n3
r3 = n3**3

print("Os resultados são {0}, {1}, {2}.".format(r1,r2,r3))
