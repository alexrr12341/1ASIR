'''Nombre:Alejandro Rodríguez Rojas

1) Queremos gestionar los precios en un supermercado para ello vamos a crear dos pequeñas funciones:

    CalcularPrecio: Esta función recibe el nombre de un artículo, su precio y la cantidad que ha comprado el cliente,
     y devuelve el precio final. Para realizar el cálculo tenemos que usar la siguiente función que nos indica si el articulo esta rebajado. 
     Si está rebajado tendremos que utilizar el 50% del precio.
    EstaRebajado: Recibe el nombre de un artículo, si el nombre contiene la palabra “Rebajas” el artículo está rebajado. Esta función devuelve si el articulo esta rebajado o no.

Crea estas dos funciones en un fichero, y a continuación crea dos programas (en dos ficheros distintos) que hagan lo siguiente:

2) Realiza un programa que vaya pidiendo artículos (nombre y precio) y la cantidad que el cliente ha comprado y te vaya mostrando el precio final
 (utilizando las funciones anteriores). El programa termina cuando introducimos un * como nombre de artículo.

3) Realiza un programa que lea el siguiente fichero de texto (el contenido es variable, y lo puedes cambiar, este es sólo un ejemplo),
 con la siguiente información: nombre del artículo, precio, cantidad comprada:

Fregona Rebajas, 4.5, 3

Detergente, 2.0, 5

Escoba, 1.5, 7'''


def CalcularPrecio(articulo,precio,cantidad):	
	preciofinal=precio*cantidad
	return articulo,preciofinal
def EstaRebajado(articulo,precio,cantidad):
	preciofinal=(precio*cantidad)*0.5
	return articulo,preciofinal
