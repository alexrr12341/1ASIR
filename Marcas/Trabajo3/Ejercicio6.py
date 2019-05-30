"""linea 1356
str(lineas[1356]).split(">")[1][:2]"""

from urllib.request import urlopen
response = urlopen('http://tiempoytemperatura.es/espana/sevilla/dos-hermanas.html')
lineas=response.readlines()
for linea in lineas:
	a=str(lineas[1356]).split(">")[1][:2]
	b=str(lineas[1361]).split(">")[1][:2]
	c=str(lineas[1362]).split(">")[1][:8]
print("Hace",a,"grados")
print("Hace",b,"% de humedad")
print("Hay",c,"de presion")