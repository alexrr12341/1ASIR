cadena1=str(input("Dime una cadena. "))
cadena2=str(input("Dime otra cadena. "))
cadena1=cadena1.upper()
cadena2=cadena2.upper()
if cadena1.find(cadena2)!=-1:
	print("La segunda cadena es una subcadena de la primera")
else:
	print("La segunda cadena no es una subcadena de la primera")