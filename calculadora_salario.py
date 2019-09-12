#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

horas_trabalho = int(input("Quantas horas você trabalhou este mês?\n"))
salario_hora = float(input("Quanto você recebe por hora trabalhada?\n"))

salario_bruto = horas_trabalho * salario_hora
IR = salario_bruto*0.11
INSS = salario_bruto*0.08
Sindicato = salario_bruto*0.05
descontos =IR + INSS + Sindicato

salario_liquido = salario_bruto - descontos

print("Sua folha salarial é: \n + Salario-Bruto: R$ {0}.\n - IR: R$ {1}.\n - INSS: R$ {2}.\n - Sindicato: R$ {3}. \n -> Salário Líquido: R$ {4}.".format(salario_bruto, IR, INSS, Sindicato, salario_liquido))  
