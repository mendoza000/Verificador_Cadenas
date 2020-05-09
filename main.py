from membrete import *
from menu import *
from fun_texto_normal import *
from fun_clave import *

opc = 0

titulo()
menu()
opc = int(input("Ingrese su opcion: "))

if (opc == 1):
	texto_normal()
	pass
elif (opc == 2):
	clave()
	pass
elif (opc == 3):
	os.system("exit")
	pass
else:
	titulo()
	menu()
	print(rojo+"¡"+reset+"Opcion incorrecta, intentelo de nuevo."+rojo+"!"+reset)
	opc = int(input("Ingrese su opcion: "))

	pass

