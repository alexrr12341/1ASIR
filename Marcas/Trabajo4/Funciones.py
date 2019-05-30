def pasar_a_segundos(hora,minuto,segundo):
	hora=3600*hora
	minuto=60*minuto
	a=hora+minuto+segundo
	return a
def calcular_coste(segundo,tarifa):
	if tarifa>0:
		tarifaSeg=tarifa*segundo
		return tarifaSeg
	else:
		print("No se ha introducido ninguna tarifa. ")	
def convertir_a_euros(tarifaEUR):
	euro=tarifaEUR//100
	centimo=tarifaEUR%100
	return euro,centimo