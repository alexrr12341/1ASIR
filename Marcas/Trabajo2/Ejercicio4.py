palabras=int(input("Digame cuantas palabras tiene la lista: "))
lista=[]
opcion=int
for p in range(1,palabras+1):
	palabra=str(input("Digame la palabra %d " %(p)))
	lista.append(palabra)
print(lista)
while opcion!=0:
	print("Elige opción:")
	print("1.Contar")
	print("2.Modificar")
	print("3.Eliminar")
	print("0.Salir")
	opcion=int(input(""))
	if opcion==1:
		palabra1=str(input("Digame la palabra a buscar: "))
		if palabra1 in lista:
			if lista.count(palabra1)>1:
				print("La palabra",palabra1,"aparece",lista.count(palabra1),"veces.")
			else :
				print("La palabra",palabra1,"aparece",lista.count(palabra1),"vez.")
		else:
			print("Esa palabra no esta en la lista.")
			palabra1=str("Digame la palabra a buscar: ")
	elif opcion==2:
		palabra=str(input("Sustituir palabra: "))
		RangoM=lista.count(palabra)
		for i in range(0,RangoM):
			lista.remove(palabra)
		palabra2=str(input("Por la palabra: "))
		for i in range(0,RangoM):
			lista.append(palabra2)
		print("La lista es ahora:",lista)
	elif opcion==3:
		palabra=str(input("Palabra a eliminar: "))
		RangoE=lista.count(palabra)
		for i in range(0,RangoE):
			lista.remove(palabra)
		print("La lista es ahora:",lista)
	elif opcion>3:
		print("Opción Incorrecta.")
if opcion==0:
	print("Adios!!!")
