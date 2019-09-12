#multa de exdecente de pesca. Valores de 50 kg limite e multa de R$ 4,00 por kg.


resposta = input("Bem vindo ao calculador de multa. Os limite de pesca continuam os mesmos (responda SIM ou NAO)?")
while resposta != 'SIM' or 'NAO':

    if resposta == 'SIM':
        limite = 50.
        break
    if resposta == 'NAO':
        limite = float(input("Quais os novos valores?"))
        break
    else:
        resposta = input("Comando nao entendido. Os limite de pesca continuam os mesmos (responda SIM ou NAO)?")


pesca = float(input("quantos quilos você pescou hoje?"))


if pesca - limite > 0:
    print("Excedente de", (pesca-limite) ,"kg. Você deverá pagar R$", (pesca - limite)*4, "reais de multa")
else:
    print("Não há excedente")
