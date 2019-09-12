#Faça um Programa que peça dois números e imprima a soma.

a = int(input("digite primeiro numero\n"))
b = int(input("digite o segundo numero\n"))

def soma(a,b):
    soma = a+ b
    return soma

total = soma(a,b)

print (total)
