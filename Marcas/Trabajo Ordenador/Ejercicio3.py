from crypt import crypt
f=open('shadow(EJ2Y3)','r')
g=open('Contraseñas(EJ3).txt','r')
lineas=f.readlines()
contraseñas=g.readlines()
nombre=str(input("Usuario: "))
# Esta es la Sal linea.split(":")[1][:12]
for linea in lineas:
	for contraseña in contraseñas:
		if nombre==linea.split(":")[0]:
			a=crypt(contraseña.split()[0],linea.split(":")[1][:12])
			if a==linea.split(":")[1]:
				print("La contraseña es:",contraseña.split()[0])
f.close()
#Probar usuario contraseña