import math
#Calcular la media de una lista

def CalcularMediaLista(lista):
	return sum(lista)/len(lista)

#Calcular media de dos numeros
def CalcularMedia(num1,num2):
	media=(num1+num2)/2
	return media

def Calculadora(num1,num2,operador):
	if operador=='+':
		return num1+num2
	elif operador=='-':
		return num1-num2
	else:
		return 0
#Funcion que reciba 2 numeros y devuelva la suma y la resta
def SumaResta(num1,num2):
	suma=num1+num2
	return num1+num2,num1-num2
#Funcion que calcule area y perimetro de una circunferencia
#Datos de entrada
def LeerRadio():
	radio=float(input('Dime el radio. '))
	return radio
#Area
def AreaCirculo(num1):
	area=math.pi*radio**2
	return area
#Perimetro
def PerimetroCirculo(num1):
	perimetro=2*math.pi*radio
	return perimetro

#Mostrar info
def Info(Num1,Num2):
	print("El area es %f y el perimetro es %f" %(area,perimetro))
#Programa Principal
"""Numero1=int(input("Dime el numero1. "))
Numero2=int(input("Dime el numero2. "))
media=CalcularMedia(Numero1,Numero2)
print(media)"""

#Programa Principal 2
"""lista1=[]
Numeros=int
while Numeros!=0:
	Numeros=int(input("Dime numeros para añadir a la lista, 0 para parar. "))
	if Numeros!=0:
		lista1.append(Numeros)
print("La media de esa lista sera: ")
mediaL=CalcularMediaLista(lista1)
print(mediaL)"""

"""lista=[[16,3],[17,5],[18,6]]
print(lista)
for lineas in lista:
	print(CalcularMediaLista(lineas[0],lineas[1]))"""
#Hacer una funcion que se llame calculadora, que recibe dos numeros y un operador, + o - , si recibe + suma, si recibe - resta

"""Numero1=int(input("Dime el numero1. "))
Numero2=int(input("Dime el numero2. "))
Operador=input("Dime el operador. " )
print(Calculadora(Numero1,Numero2,Operador))"""

#Tenemos un fichero con el siguiente contenido
"""2
3
+"""
#Mostramos por pantalla lo que tenemos en el fichero

"""f=open('fich.txt')
lineas=f.readlines()
f.close()
Numero1=int(lineas[0].replace('\n',''))
Numero2=int(lineas[1].replace('\n',''))
Operador=(lineas[2].replace('\n',''))
print(Numero1,'+',Numero2,'=',end="")
print('',Calculadora(Numero1,Numero2,Operador))"""

#Hacer una funcion que reciba 2 numeros y devuelva la suma y la resta
"""Numero1=int(input("Dime el numero1. "))
Numero2=int(input("Dime el numero2. "))
s,r=SumaResta(Numero1,Numero2)
print(s)
print(r)"""

"""radio=LeerRadio()
area=AreaCirculo(radio)
perimetro=PerimetroCirculo(radio)
Info(area,perimetro)"""

