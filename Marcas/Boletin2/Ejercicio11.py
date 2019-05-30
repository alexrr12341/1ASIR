#Calcular los dias julianos
#Dia juliano del 31/12/2019 es 365
#22/5/2019, Enero(31)+Febrero(28)+Marzo(31)+Abril(30)+Dia(22)
#Funcion LeerFecha(3 enteros)

def EsBisiesto(year):
	if (year % 4 == 0 and not (year % 100 == 0)) or year % 400 == 0:
		Bisiesto = True
	else:
		Bisiesto = False

#Return [dia,mes,year]

def DiaDelMes(mes,year):
	if Bisiesto:
		if mes in [1,3,5,7,8,10,12]:
			return 31
		elif mes == 2:
			return 29
		elif mes in [4,6,9,11]:
			return 30

	else:
		if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
			return 31
		elif mes==2:
			return 28
		elif mes==4 or mes==6 or mes==9 or mes==11:
			return 30
def LeerFecha(dia,mes,year):
	dia=int("Dime el dia. ")
	mes=int("Dime el mes. ")
	year=int("Dime el year. ")
	return [dia,mes,year]

def ValidarFecha(dia,mes.year):
	for Numeros in [dia,mes,year]:
		if mes==1, 
