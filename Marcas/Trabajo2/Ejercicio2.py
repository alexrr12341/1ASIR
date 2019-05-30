cadena1=str(input("Dime una cadena. "))
Repetido=False
for caracter in cadena1:
	caracter=cadena1.count(caracter)
	if caracter>1:
		Repetido=True
if Repetido:
	print("Se repite un caracter.")
else:
	print("No se repite ningun caracter.")