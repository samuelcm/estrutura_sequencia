#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
#calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura = float(input("Qual sua altura?\n"))
peso_ideal = (72.7*altura) - 58
#peso_ideal = round(peso_ideal, 2)

print("Seu peso ideal é {peso}.".format(peso = peso_ideal))
