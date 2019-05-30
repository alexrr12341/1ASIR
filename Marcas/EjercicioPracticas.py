#Declaramos diccionario para guardar precios de distintas frutas
#Programa pide nombre de la fruta y la cantidad que hay
#Nombre precio
dic={'pera':5,'platano':4,'piña':3,'manzana':2}
while True:
	fruta=str(input("¿Que fruta te gustaría seleccionar? "))
	cantidad=int(input("¿Cuanta cantidad has comprado? "))
	if fruta in dic:
		print(dic[fruta]*cantidad)
	else:
		print("No existe la fruta.")
	resp=input("¿Quieres introducir otra fruta? (S o N) ")
	if resp.lower()!="s" or resp.lower()!="n":
		print("Error.")
		resp=input("¿Quieres introducir otra fruta? (S o N) ")
	else:
		if resp.lower()=="n":
			break