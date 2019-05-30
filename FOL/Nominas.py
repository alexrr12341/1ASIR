SB=float("¿Cual es el salario base? ")
Grupo=Int("¿Cual es el numero de grupo? ")
ContadorC=0
if Grupo>0 and Grupo<=7:
	print("30 dias")
else:
	print("28,29,30,31 dias")
IRPF=Float("¿Cuanto es el IRPF? ")

Complementos=int("¿Cuantos complementos tiene? ")
for dinero in range(1,Complementos+1):
	Complemento=float("Dime el precio del complemento. ")
	ContadorC+=Complemento
print("El total de complementos es:",ContadorC)
HorasExtras=float(input("Dime lo que pagas por horas extras" ))
