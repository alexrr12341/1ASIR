#CREAR PROGRAMA QUE PERMITA GUARDAR LOS NOMBRES DE ALUMNOS Y SUS NOTAS
#CADA ALUMNO TIENE DISTINTA CANTIDAD DE NOTAS
cantidad=int(input("Dime la cantidad de alumnos. "))
alumnos=[]
for i in range(cantidad):
	alumno={}
	alumno['nombre']=input("Dime el nombre del alumno. ")
	alumno['notas']=[]
	nota=int(input("Dime la nota: (negativo para salir) "))
	while nota>=0:
		alumno['notas'].append(nota)
		nota=int(input("Dime la nota: (negativo para salir) "))
	alumnos.append(alumno)
for alumno in alumnos:
	print(alumno['nombre'],(sum(alumno['notas'])/len(alumno['notas'])))
#Me pide el nombre de un alumno y me muestra las notas
buscar=input("Nombre del alumno a buscar. ")
esta_alumno=False
for alumno in alumnos:
	if alumno['nombre']==buscar:
		esta_alumno=True
		for nota in alumno['notas']:
			print(nota,end="|")
		print()
if not esta_alumno:
	print("El alumno buscado no está.")
#Mostrar el alumno o los alumnos que han sacado la maxima nota. (lista)

for alumno in alumnos:
	if alumno['notas']==max(notas):
		print(alumno['notas'])