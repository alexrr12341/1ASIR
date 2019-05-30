lista1=[]
palabras1=int(input("Dime cuántas palabras tiene la primera lista: "))
for i in range(0,palabras1):
	palabra1=str(input("Dime una palabra: "))
	lista1.append(palabra1)
print("La primera lista es: ",lista1)
lista1M=[]
for i in range(0,palabras1):
	if lista1.count(lista1[i])>=2:
		lista1M.append(lista1[i])
for i in range(0,len(lista1M)):
	if lista1.count(lista1M[i])>1:
		lista1.remove(lista1M[i])
lista2=[]
palabras2=int(input("Dime cuántas palabras tiene la segunda lista: "))
for i in range(0,palabras2):
	palabra2=str(input("Dime una palabra: "))
	lista2.append(palabra2)
print("La segunda lista es: ",lista2)
lista2M=[]
for i in range(0,palabras2):
	if lista2.count(lista2[i])>=2:
		lista2M.append(lista2[i])
for i in range(0,len(lista2M)):
	if lista2.count(lista2M[i])>1:
		lista2.remove(lista2M[i])
listaC=[]
lista3=[]
lista4=[]
listaTotal=[]
for i in range(0,len(lista2)):
	if lista2[i] in lista1:
		listaC.append(lista2[i])
	else:
		lista3.append(lista2[i])
	listaTotal.append(lista2[i])
for i in range(0,len(lista1)):
	if lista1[i] not in lista2:
		lista4.append(lista1[i])
		listaTotal.append(lista1[i])
print("Palabras que aparecen en las dos listas: ",listaC)
print("Palabras que sólo aparecen en la primera lista:	",lista4)
print("Palabras que sólo aparecen en la segunda lista:	",lista3)
print("Todas las palabras: ",listaTotal)