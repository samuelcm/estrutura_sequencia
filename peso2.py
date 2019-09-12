#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7



sexo = str(input("Calculadora de peso ideal.\n Se você for homem digite 'h'\n Se for mulher digite 'm'\n"))
altura = float(input("Qual sua altura?"))
peso_h = (72.7*altura) - 58
peso_m = (62.1*altura) - 44.7

if sexo == "h":
  print("Seu peso ideal é {peso}.".format(peso=peso_h))
else:
  print("Seu peso ideal é {peso}.".format(peso = peso_m))

#72.7*altura) - 58
