#Hacer un programa en python que me muestre la lista de usuarios que hay en el ordenador

#with open('/etc/passwd','r') as archivo:
#	lineas=archivo.readlines()
f=open('/etc/passwd','r')
lineas=f.readlines()
UID=str(input("Dime el UID de la cadena. "))
UIDi=False
for linea in lineas:
	datos=linea.split(':')
	if UID==datos[2]:
		print(datos[0])
		UIDi=True

f.close()
if not UIDi:
	print("No existe el usuario.")