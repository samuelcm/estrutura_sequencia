#Faça um Programa que pergunte quanto você ganha por hora e o
#número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input("Calculador de salário. \n Quanto voce ganha por hora?\n"))
horas_trabalho = int(input("quantas horas você trabalhou esse mês?\n"))

print("Você receberá R$ {salario} de salário este mês.".format(salario = salario_hora*horas_trabalho))
