from lxml import etree





    #1 Función que devuelve una lista con los nombres de las provincias.
def nombreprovincia(doc):
    lista = doc.xpath("//nombre/text()")
    return lista
    #2 Función que devuelve una lista con todos las poblaciones.
def nombrepoblaciones(doc):
    lista = doc.xpath("//localidad/text()")
    return lista
    #3 Función que devuelve las provincias y el total de poblaciones que tiene cada uno. Piensa la estructura de datos que va a devolver la función.
def lista_provincias_total_poblaciones(doc):
    lista=[]
    nombres= doc.xpath('//nombre/text()')
    for provincia in doc.xpath('//provincia'):
        num_localidades=provincia.xpath('count(./localidades/localidad)')
        lista.append(int(num_localidades))
    return zip(nombres,lista)
    #4 Función que recibe el nombre de una provincia y devuelve la lista de poblaciones.
def poblaciones(prov,doc):
    nombres = doc.xpath('//provincia[nombre="%s"]//localidad/text()'%prov)
    return nombres
    #5 Función que recibe el nombre de una población y te devuelve la provincia donde se encuentra.
def provincias(pobl,doc):
    nombre = doc.xpath('//nombre/localidades[localidad="%s"]/../nombre/text()'%pobl)
    return nombre[0]
    #6 Función que recibe una lista distintos identificadores de provincias, y te devuelve las provincias que corresponden a cada identificador, y sus poblaciones.
    #7 Función que reciba el nombre de una provincia devuelva las “ciudades grandes” (atributo c=”1”).
    #8 Función que reciba una localidad y te devuelva si es “ciudad grande” (atributo c=”1”) o no de provincia. Si es “ciudad grande” de provincia te devuelve el nombre de la provincia.

doc=etree.parse('provinciasypoblaciones.xml')

opciones='''1.Nombre de Provincias
2.Todas Poblaciones
3.Provincias y Total de Localidades
4.Preguntar Provincia y dar localidades
5.Preguntar Localidad y dar provincia
0.Salir'''
opcion=int
while opcion!=0:
    print(opciones)
    opcion=int(input("Dime la opción. "))
    if opcion==1:
        for prov in nombreprovincia(doc):
            print(prov)  
    elif opcion==2:
        for pobl in nombrepoblaciones(doc):
            print(pobl)
    elif opcion==3:
        for nombre,total in lista_provincias_total_poblaciones(doc):
            print(nombre,total)
    elif opcion==4:
        provincia=str(input("Dime el nombre de la provincia. "))
        for nombre in poblaciones(provincia,doc):
           print (nombre)
    elif opcion==5:
        localidad=str(input("Dime el nombre de la localidad. "))
        for nombre in poblaciones(localidad,doc):
            print(nombre)


'''Crea en otro fichero el programa principal que te muestre el siguiente menú:

    1 Mostrar todas las provincias: Muestra por pantalla el nombre de todas las provincias.
    2 Mostrar todas las poblaciones: Muestra por pantalla el nombre de todas las poblaciones.
    3 Mostrar provincias y número de poblaciones: Muestra por pantalla el nombre de todas las provincias y la cantidad de poblaciones.
    4 Mostrar las poblaciones: Lee una provincia por teclado y te muestra el nombre de las poblaciones. Si la provincia no existe te da un error.
    5 Mostrar la provincia: Lee una población por teclado y te muestra el nombre de la provincia. Si la población no existe te da un error.
    6 Información por identificador: Pide un conjunto de identificadores de provincias, y te muestra por pantalla las provincias correspondientes y sus poblaciones.
    7 Ciudades grandes: Lee una provincia por teclado y te muestra las poblaciones grandes (“ciudades grandes”). Si la provincia no existe te da un error.
    8 Es ciudad grande: Lee una población y si es ciudad grande te muestra el nombre de la provincia, sino te dice que no es una ciudad grande.'''
