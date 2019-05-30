lista=[]
nombre=str(input("Dime el nombre. "))
while nombre!="*":
	edad=int(input("Dime la edad."))
	lista.append(nombre)
	lista.append(edad)
	nombre=str(input("Dime el nombre. "))
contador=0
maximo=lista[1]
for rango in range(0,len(lista)):
	if rango%2!=0 and lista[rango]>maximo:
		maximo=lista[rango]
	if rango%2!=0:
		contador=contador+lista[rango]
for rango in range(0,len(lista)):
	if maximo==lista[rango]:
		if len(lista[rango-1])>=6:
			print(lista[rango-1]," ",lista[rango])
		else:
			print(lista[rango-1]," ",lista[rango])
media=contador/(len(lista)/2)
print("Media:",media)
nombre=str(input("Dime un nombre para buscar: "))
Busqueda=False
print("Lista de alumnos con nombre: ",nombre)
for rango in range(0,len(lista)):
	if nombre==lista[rango]:
		if len(lista[rango])>=6:
			print(lista[rango]," ",lista[rango-1])
		else:
			print(lista[rango]," ",lista[rango-1])
		Busqueda=True
if Busqueda:
	print(lista.count(nombre),"alumnos que se llaman como:",nombre)
else:
	print("El nombre:",nombre,"no figura en la lista.")
print("Lista de alumnos mayores de edad:")	
for rango in range(0,len(lista)):
	if rango%2!=0 and lista[rango]>=18:
		if len(lista[rango-1])>=6:
			print(lista[rango-1]," ",lista[rango])
		else:
			print(lista[rango-1]," ",lista[rango])