#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

numero = input("Digite um número\n")

try:
    numero=float(numero)
    print("o numero informado foi", numero)
except:
    print("o valor digitado nao corresponde a um numero")
