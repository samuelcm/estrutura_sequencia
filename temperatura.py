#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.

F = float(input("Qual a temperatura em Farenheit neste momento?"))
C = (5 * (F-32) / 9)
C = round(C,2)
print("A temperatura em Celsius neste momento é ", C)

if C > 30.:
  print ("Tá quente. Vá para a praia")
  if C < 30 and C > 20:
    print("A temperatura está boa")
else:
    print("Tá frio. Volte para a cama")
