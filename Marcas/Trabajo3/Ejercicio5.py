
'''dar la url de la ciudad {nombre}
Tener la URL Y AÑADIRLE PRIMERO LO SEGUNDO Y DESPUES LO PRIMERO

Conclusiones:SI la informacion que esta guardada en un fichero tiene una estructura

Primero hacer un split separado por comas
Nombre ciudad
-------------
ciudad.split(',')
ciudad.split(',')[1].split(":")[1].strip()[1:-1]
ciudad.split('"')[7]

LatitudLongitud
---------------
ciudad.split(',')[2]
ciudad.split('"')[10]
ciudad.split('"')[10].split(',').split'''


f=open('zips(EJ5)','r')
lineas=f.readlines()
contador=0

print(contador)
print("Hay",len(lineas),"codigos")

ciudad=str(input("Dime la ciudad Que deseas buscar "))

for linea in lineas:
	if ciudad==linea.split(',')[1].split('"')[3]:
		a=linea.split(',')[3].replace(" ]","").replace(" ","")
		b=linea.split(',')[2].split(":")[1].replace(" [ ","")
		print("Ciudad Encontrada.")
		print("http://www.openstreetmap.org/#map=19/",end="")
		print(a,end="")
		print("/",end="")
		print(b)
