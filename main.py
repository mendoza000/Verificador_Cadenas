"""
	@Author: Omar_Mendoza.
	@Version: 1.3.
	Web: github.com/OmarMendozaDev/Verificador_Cadenas/
"""


# Importa funciones de otros archivos para estar mas ordenado.
from color import *
from fun_clave import *
from fun_texto_normal import *
from menu import *
from title import *

# Variables esenciales.
opc = 0
fails = 0
alert = (am+"["+ro+"!"+am+"] "+re)
salt = ("\n")

# Se llaman funciones externas...
titulo()
menu()

# while para verificar lo que ingrese el usuario
# soporta numeros incorrectos y letras.
while True:

	# Cuenta las veces que ha fallado el usuario
	# Si falla muchas veces, el programa se cierra.
	if (fails > 2):
		print(alert+"Realizo muchos intentos fallidos, el programa finalizara.")
		os.system("pause")
		break;
		
	# Se verifican si lo ingresado es correcto
	try:
		opc = int(input("Ingrese su opcion: "))

		if(opc < 0 or opc > 3):
			print(salt+alert+"Solo estan habilitadas las opciones '1', '2' y '3'")
			print(alert+"Intente nuevamente."+salt)
			fails = fails +1
			continue
		else:
			break
	# Si se obtiene un error por ingresar cadenas, el programa pide nuevamente que se ingrese la opcion, se suma el fallo.
	except ValueError:
		print(salt+alert+"No se admiten letras, solo numeros de 1 a 3")
		print(alert+"Intente nuevamente."+salt)
		fails = fails +1

# Se ejecutan funciones segun la opcion.
if (opc == 1):
	texto_normal()
	pass
if (opc == 2):
	clave()
	pass
if (opc == 3):
	os.system("cls")
	titulo()
	print(ve+"	¡Gracias por probar mi programa :D!\n"+re)
	os.system("pause")
	pass

