# @Author: Omar_Mendoza.
# @Version: 1.2
# web: github.com/OmarMendozaDev/Verificador_Cadenas/

from title import *
from menu import *
from fun_texto_normal import *
from fun_clave import *
from color import *

opc = 0
fails = 0
alert = (am+"["+ro+"!"+am+"] "+re)
salt = ("\n")

titulo()
menu()
opc = int(input("Ingrese su opcion: "))

while (opc > 3 or opc <= 0):

	print(salt+alert+"Opcion incorrecta.")

	if (fails > 2):
		print(alert+"Realizo muchos intentos fallidos, el programa finalizara.")
		os.system("pause")
		break;
		
	opc = int(input("Ingrese su opcion: "))
	fails = fails +1

	pass

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

