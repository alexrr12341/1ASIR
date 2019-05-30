import json
with open('books.json') as fichero:
	datos=json.load(fichero)

for libro in datos['bookstore']['book']:
	if type(libro['author'])==str:
		print(libro['author'])
	else:
		for author in libro['author']:
			print(author)