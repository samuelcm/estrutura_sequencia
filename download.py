#Faça um programa que peça o tamanho de um arquivo para download (em MB)
#e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo
#aproximado de download do arquivo usando este link (em minutos).

arquivo_tamanho = float(input("Qual o tamanho do arquivo para download?\n"))
velocidade = float(input("Qual a velocidade de sua internet\n"))

tempo_download_s = arquivo_tamanho/velocidade
tempo_download_m = tempo_download_s/60
download_m = round(tempo_download_m,2)


print("O tempo de download de seu arquivo é de {0} minutos.".format(download_m))
#print("O tempo de download de seu arquivo é de {0} segundos.".format(tempo_download_s))
