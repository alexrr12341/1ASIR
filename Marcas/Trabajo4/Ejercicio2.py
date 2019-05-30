import Funciones
f=open('Fichero','r')
lineas=f.readlines()
contador=0
fichero=open('Fichero','r')
linea = 0
for lineas in fichero:
    if linea == 0:
        tarifa = int(lineas.replace("\n","").split(" ")[1])
        print("La tarifa expuesta es de ",tarifa,"centimos.")
        linea = linea + 1
    else:
        horas=int(lineas.split(":")[0])
        minutos=int(lineas.split(":")[1])
        segundos=int(lineas.split(":")[2].replace("\n",""))
        segundosE=Funciones.pasar_a_segundos(horas,minutos,segundos)
        contador+=Funciones.pasar_a_segundos(horas,minutos,segundos)
        tarifas=Funciones.calcular_coste(segundosE,tarifa)
        tarifasEU=Funciones.convertir_a_euros(tarifas)
        print("Su comunicación ha durado",segundosE,"segundos.")
        print("Su comunicación ha costado",tarifasEU[0],"euros y",tarifasEU[1],"centimos.")

CosteT=Funciones.calcular_coste(contador,tarifa)
EurosT=Funciones.convertir_a_euros(CosteT)
print("Las comunicaciones totales han durado",contador,"segundos")
print("Las comunicaciones totales han costado",EurosT[0],"euros y",EurosT[1],"centimos.")

