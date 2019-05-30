import Examen

'''3) Realiza un programa que lea el siguiente fichero de texto (el contenido es variable, y lo puedes cambiar, este es sólo un ejemplo),
 con la siguiente información: nombre del artículo, precio, cantidad comprada:'''

'''Fregona Rebajas, 4.5, 3

Detergente, 2.0, 5

Escoba, 1.5, 7'''
#Abrimos el fichero para leer
f=open('FicheroExamen','r')

Lista=f.readlines()
#Leemos las lineas de la lista
for precios in Lista:
	Nombre=precios.split(',')[0].split(' ')[0]
	Precio=float(precios.split(',')[1].replace(" ",""))
	Cantidad=int(precios.split(',')[2].replace("\n","").replace(" ",""))
	#Hacemos que si la palabra contiene Rebajas utilice la funcion Esta rebajado y si no, no la utilice
	if precios.split(',')[0].split(' ')[-1]=='Rebajas':
		print("El producto",Examen.EstaRebajado(Nombre,Precio,Cantidad)[0],"ha costado",Examen.EstaRebajado(Nombre,Precio,Cantidad)[1],"euros en total rebajado.")
	else:
		print("El producto",Examen.CalcularPrecio(Nombre,Precio,Cantidad)[0],"ha costado",Examen.CalcularPrecio(Nombre,Precio,Cantidad)[1],"euros en total.")


	