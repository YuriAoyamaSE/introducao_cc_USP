segundos_totais = int(input("Por favor, entre com o número de segundos que deseja converter: "))
segundos = segundos_totais % 60
minutos = segundos_totais // 60
horas = minutos // 60
minutos = minutos % 60
dias = horas // 24
horas = horas % 24

print(f"{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos.")