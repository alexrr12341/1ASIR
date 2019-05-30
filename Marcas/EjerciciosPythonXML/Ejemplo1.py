import json
with open('books.json') as fichero:
	datos=json.load(fichero)

for libro in datos['bookstore']['book']:
	print(libro['author'])