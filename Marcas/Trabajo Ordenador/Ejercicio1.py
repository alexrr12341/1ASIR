
#1-Leer el numero de cuenta(str) 20 posiciones
#2-Crear una lista con los 8 primeros numeros y dos ceros a la izquierda Primera lista [0,0,A,A,A,A,B,B,B,B]
#3-Calculamos el codigo de control 1 y comprobamos si es correcto.
#4 y #5-LO MISMO PERO CON LOS 10 DIGITOS DE NUMERO DE CUENTAS


"""Calcula el dígito de control de una CCC.
Recibe una lista con 10 numeros enteros y devuelve el DC
correspondiente"""
def calcula_dc(lista):
	pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
	aux = []
	for i in range(10):
		aux.append(lista[i]*pesos[i])
	resto = 11 - sum(aux) %11
	if resto == 10:
		return 1
	elif resto == 11:
		return 0
	else:
		return resto

indicadorCCC=False
indicadorcad=False
lista=[0,0]
lista2=[]
lista3=[]
CCC=str(input("Escriba su CCC para comprobar su validez. (AAAA-BBBB-CC-DDDDDDDDDD). "))
if len(CCC)==20:
	indicadorcad=True
else:
	print("La cadena no es correcta.")
if indicadorcad:
	for cadena in CCC[:10]:
		if len(lista)<10:
			lista.append(cadena)
	for cadena2 in CCC:
		if len(lista3)<10:
			lista3.append(cadena2)
		else:
			lista2.append(cadena2)
	listaINT=[int(i) for i in lista]
	listaINT2=[int(i) for i in lista2]
	a=calcula_dc(listaINT)
	b=calcula_dc(listaINT2)
	if str(a)==CCC[8] and str(b)==CCC[9]:
		print("Codigo Correcto. ")
	else:
		print("Codigo Incorrecto. ")

f=open('bancos(EJ1).txt','r')
lineas=f.readlines()
Entidad=CCC[0]+CCC[1]+CCC[2]+CCC[3]
for codigo in lineas:
	if codigo.split(',')[0]==Entidad:
		print(codigo.split(',')[1])

f.close()
'''notas={'LM' 9,'ISO'7}
   listas=["LM","ISO"]
   for asignaturas in lista:
   	print(notas(asignaturas))'''

#00491500051234567892






































































































































































































