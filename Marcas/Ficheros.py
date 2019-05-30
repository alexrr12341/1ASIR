f=open('ficheros.txt','r')
lineas=f.readlines()
for linea in lineas:
	datos=linea.split(',')
	print(datos[0],"tiene",datos[1],"años")
	

f.close()

