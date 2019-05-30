import Funciones
comunicacion=int(input("¿Cuantas comunicaciones se han realizado? "))
contador=0
Comunicacion=False
if comunicacion>0:
	Comuniacion=True
	for i in range(1,comunicacion+1):
		tarifas=int(input("Dime la tarifa(centimos por segundo) "))
		horas=int(input("Dime la cantidad de horas. "))
		minutos=int(input("Dime la cantidad de minutos. "))
		segundos=int(input("Dime la cantidad de segundos. "))
		if horas>=0:
			if minutos>=0 and minutos<60:
				if segundos>=0 and segundos<60:
					segundos2=Funciones.pasar_a_segundos(horas,minutos,segundos)
					tarifas2=Funciones.calcular_coste(segundos2,tarifas)
					tarifasEU=Funciones.convertir_a_euros(tarifas2)
					print("Su comunicacion ha durado",segundos2,"segundos.")
					print("Su comunicacion ha costado",tarifasEU[0],"euros y",tarifasEU[1],"centimos.")
					contador+=tarifas2
ContadorT=Funciones.convertir_a_euros(contador)
if not Comunicacion:
	print("El total de comunicaciones ha costado",ContadorT[0],"euros y",ContadorT[1],"centimos.")
