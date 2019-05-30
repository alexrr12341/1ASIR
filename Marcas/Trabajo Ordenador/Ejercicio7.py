DineroT=float(input("Dime la cantidad total. "))
DineroE=float(input("Dime la cantidad entregada. "))
DineroC=float
contador500=0
contador200=0
contador100=0
contador50=0
contador20=0
contador10=0
contador5=0
contador2=0
contador1=0
contador050=0
contador020=0
contador010=0
contador005=0
contador002=0
contador001=0
if DineroT>DineroE:
	print("Has entregado menos que lo pedido.")
	DineroT=float(input("Dime la cantidad total. "))
	DineroE=float(input("Dime la cantidad entregada. "))
else:
	print("Cantidad total:",DineroT,"€")
	print("Cantidad entregada:",DineroE,"€")

	DineroD=DineroE-DineroT
	print("Cantidad a devolver:",DineroD,"€")
	while DineroD>=500:
		contador500+=1
		DineroD=DineroD-500
	while DineroD>=200:
		contador200+=1
		DineroD=DineroD-200
	while DineroD>=100:
		contador100+=1
		DineroD=DineroD-100
	while DineroD>=50:
		contador50+=1
		DineroD=DineroD-50
	while DineroD>=20:
		contador20+=1
		DineroD=DineroD-20
	while DineroD>=10:
		contador10+=1
		DineroD=DineroD-10
	while DineroD>=5:
		contador5+=1
		DinerdoD=DineroD-5
	while DineroD>=2:
		contador2+=1
		DineroD=DineroD-2
	while DineroD>=1:
		contador1+=1
		DineroD=DineroD-1
	while DineroD>=0.50:
		contador050+=1
		DineroD=DineroD-0.50
	while DineroD>=0.20:
		contador020+=1
		DineroD=DineroD-0.20
	while DineroD>=0.10:
		contador010+=1
		DineroD=DineroD-0.10
	while DineroD>=0.05:
		contador005+=1
		DineroD=DineroD-0.05
	while DineroD>=0.02:
		contador002+=1
		DineroD=DineroD-0.02
	while DineroD>=0.001:
		contador001+=1
		DineroD=DineroD-0.01
if contador500>0:
	if contador500==1:
		print(contador500,"billete de 500€")
	if contador500>1:
		print(contador500,"billetes de 500€")
if contador200>0:
	if contador200==1:
		print(contador200,"billete de 200€")
	if contador200>1:	
		print(contador200,"billetes de 200€")
if contador100>0:
	if contador100==1:
		print(contador100,"billete de 100€")
	if contador100>1:
		print(contador100,"billetes de 100€")
if contador50>0:	
	if contador50==1:
		print(contador50,"billete de 50€")
	if contador50>1:
		print(contador50,"billetes de 50€")
if contador20>0:
	if contador20==1:
		print(contador20,"billete de 20€")
	if contador20>1:
		print(contador20,"billetes de 20€")
if contador10>0:
	if contador10==1:
		print(contador10,"billete de 10€")
	if contador10>1:
		print(contador10,"billetes de 10€")
if contador5>0:
	if contador5==1:
		print(contador5,"billete de 5€")
	if contador5>1:
		print(contador5,"billetes de 5€")
if contador2>0:
	if contador2==1:
		print(contador2,"moneda de 2€")
	if contador2>1:
		print(contador2,"monedas de 2€")
if contador1>0:
	if contador1==1:
		print(contador1,"moneda de 1€")
	if contador1>1:
		print(contador1,"monedas de 1€")
if contador050>0:
	if contador050==1:
		print(contador050,"moneda de 50 centimos")
	if contador050>1:
		print(contador050,"monedas de 50 centimos")
if contador020>0:
	if contador020==1:
		print(contador020,"moneda de 20 centimos")
	if contador020>1:
		print(contador020,"monedas de 20 centimos")
if contador010>0:
	if contador010==1:
		print(contador010,"moneda de 10 centimos")
	if contador010>1:
		print(contador010,"monedas de 10 centimos")
if contador005>0:
	if contador005==1:
		print(contador005,"moneda de 5 centimos")
	if contador005>1:
		print(contador005,"monedas de 5 centimos")
if contador002>0:
	if contador002==1:
		print(contador002,"moneda de 2 centimos")
	if contador002>1:
		print(contador002,"monedas de 2 centimos")
if contador001>0:
	if contador001==1:
		print(contador001,"moneda de 1 centimo ")
	if contador001>1:
		print(contador1,"monedas de 1 centimo")
