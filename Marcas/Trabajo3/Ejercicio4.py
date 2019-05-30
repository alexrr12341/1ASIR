def notamedia(lista):
	return sum(lista)/len(lista)

f=open('EjercicioAlumnos','r')
alumnos=f.readlines()
alumnos2=[]
for alumno in alumnos:
	alumnos2.append(alumno.replace("\n",""))
print(alumnos2)

for lineas in alumnos2:
	