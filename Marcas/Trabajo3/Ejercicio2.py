#La sal son los 12 primeros caracteres
from crypt import crypt
f=open('shadow(EJ2Y3)','r')
lineas=f.readlines()

nombre=str(input("Usuario: "))
contraseña=str(input("Contraseña: "))

# Esta es la Sal linea.split(":")[1][:12]
for linea in lineas:
	if nombre==linea.split(":")[0]:
		a=crypt(contraseña,linea.split(":")[1][:12])
		if a==linea.split(":")[1]:
			print("Usuario valido. ")
		else:
			print("Usuario invalido. ")

#probar prueba/asdasd