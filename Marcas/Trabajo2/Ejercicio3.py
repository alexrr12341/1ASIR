indicador=False
temperaturas='''Utrera,29,12
Dos Hermanas,32,14
Sevilla,30,15
Alcalá de Guadaíra,31,14
'''
datosunidos= temperaturas.splitlines()
print(datosunidos)
Temperatura=False
for lineas in datosunidos:
	print(lineas.split(",")[0],(int(lineas.split(",")[1])+int(lineas.split(",")[2]))/2)
ciudad=str(input("Dime la ciudad. "))
for lineas in datosunidos:
	if ciudad==lineas.split(",")[0]:
		Temperatura=True
		print("Temperatura máxima->",lineas.split(",")[1])
		print("Temperatura mínima->",lineas.split(",")[2])

if not Temperatura:
	print("Error, la ciudad no existe.")