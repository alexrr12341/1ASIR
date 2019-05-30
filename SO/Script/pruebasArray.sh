#!/bin/bash

typeset -a Array	# Declaramos el array

Array[23]="HolaAmigos"

exec 3< ./Fichero.txt

Contador=1
while read linea <&3; do
	
	echo "$Contador  -  $linea"
	Array[$Contador]="$linea"		# Añadimos elementos al array

done

while true; do

	read -p "¿Que sistema quieres?" Opcion

	case "$Opcion" in
	"0")
		break
	;;
	"1")
		#Comandos a ejecutar
		Array[$Opcion]
	;;
	"2")
		#Comandos a ejecutar
	;;
	"n")
		#Comandos a ejecutar
	;;
	*)
		#No está en la lista.
	esac

done

for elemento in ${Array[*]}; do		# Recorremos el array

	echo $elemento

done

echo ${Array[3]}

echo ${Array[23]}	# Muestra el elemento de la posicion 23

echo ${Array[*]}	# Muestra todos los elementos, lo mismo que @

echo ${Array[@]:6:5}	# Muestra 5 elementos del array, desde la posición 6



echo ${#Array[@]}	# Muestran la longitud del array
echo ${#Array[*]}
