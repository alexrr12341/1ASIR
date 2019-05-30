import Funciones
'''2) Realiza un programa que vaya pidiendo artículos (nombre y precio) y la cantidad que el cliente ha comprado y te vaya mostrando el precio final
    (utilizando las funciones anteriores). El programa termina cuando introducimos un * como nombre de artículo.'''

#Pedimos el nombre
Nombre=str

#Hacemos el bucle while para que cuando pongamos * se acabe el programa
while Nombre!='*':
	Nombre=str(input("¿Cual es el nombre del artículo? "))
	Precio=float(input("¿Cual es el precio del artículo? "))
	Cantidad=int(input("Dime la cantidad de productos comprados. "))
	if Nombre!='*':
		#Printeamos el Nombre del producto junto a su precio final
		print("El producto",Funciones.CalcularPrecio(Nombre,Precio,Cantidad)[0],"ha costado",Funciones.CalcularPrecio(Nombre,Precio,Cantidad)[1],"euros en total.")
print("Fin del programa.")

