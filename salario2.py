#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

hora_salario = input("Quanto você recebe de salário?")
num_horas = int(input("Quantas horas trabalhadas?"))

try:
    hora_salario = float(hora_salario)
    if hora_salario*num_horas != 0:
         print("Seu salário é {produto}.".format(produto = hora_salario*num_horas))
    else:
        print("Digite um numero diferente de zero")
except:
    print("digite um numero válido")
    quit()
