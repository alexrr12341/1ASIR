import json

for prov in datos['lista']['provincia']:
	print(prov['nombre']['__cdat']
	if type(prov['localidades']['localidad'])==list:
		print(len(prov['localidades']['localidad']))
	else:
		print(1)