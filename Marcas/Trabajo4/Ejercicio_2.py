#Necesitamos que se facture el uso de un teléfono.
#Nos informarán de la tarifa por segundo (en céntimos), cuántas comunicaciones se realizaron,
#la duración de cada comunicación expresada en horas, minutos y segundos.
#Como resultado deberemos informar la duración en segundos de cada comunicación y su costo.

#Vamos a dividir este problemas en problemas más pequeños:

    #Cada comunicación se expresa en horas, minutos y segundos, la tarifa es € por segundos,
    #por lo tanto lo primero que vamos a solucionar es convertir las horas, minutos y segundos en segundos.
    #Para ello vamos a crear una función llamada pasar_a_segundos.
    #Piensa los parámetros de entrada que tiene esta función yel valor que devuelve. ¿De qué tipo son?
    #Una vez que sabemos los segundos que ha tardado una comunicación y la tarifa por segundo
    #vamos a crear una función llamada calcular_coste que nos calcule cuanto cuesta, en céntimos, la llamada.
    #Piensa los parámetros y el valor devuelto de la función.
    #Por último vamos a crear una función para convertir el coste en céntimos, en una cantidad de dinero expresada en euros y céntimos.
    #Para ello creamos la función convertir_a_euros. Piensa los parámetros de entrada y los valores devueltos.

    #Realiza un programa que te informe de cuanto vale cada comunicación
    #y el total de dinero de todas las comunicaciones.
    #En esta ocasión los datos de la duración de las comunicaciones y la tarifa por segundos
    #se encuentran en este fichero donde en la primera línea te encuentras la tarifa,
    #y en las restantes la duración de cada una de las comunicaciones expresadas en horas, minutos y segundos.


def pasar_a_segundos(duracion):

    hh = int(duracion.split(":")[0])
    mm = int(duracion.split(":")[1])
    ss = int(duracion.split(":")[2])
    S = 0
    S = hh * 3600 + mm * 60 + ss
    return S

def calcular_coste(segundos,tarifa):

    coste = segundos * tarifa
    return round(coste,2)

def convertir_a_euros(coste):

    euros = coste // 100
    return euros

lista = []
fichero=open('Fichero','r')
i = 0
for linea in fichero:
    if i == 0:
        tarifa = int(linea.replace("\n","").split(" ")[1])
        print("La tarifa de cada comunicación es de",tarifa,"cent.")
        i = i + 1
    else:
        lista.append(pasar_a_segundos(str(linea)))
segundos = 0
for i in range(0,len(lista)):
    segundos = segundos + int(lista[i])

costetotal = convertir_a_euros(calcular_coste(segundos,tarifa))
print("El coste total de todas las comunicaciones es de",costetotal,"€ y",costetotal%100,"cent.")
