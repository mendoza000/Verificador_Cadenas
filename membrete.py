from color import *
import os

# ---Colores---
verde    = Green
rojo     = Red
reset    = Reset
amarillo = Yellow
# -------------

def titulo():
	os.system("cls")
	print (amarillo+"		-------------------------------------"+reset)
	print (amarillo+"		|"+reset+"        Analizador de cadenas      "+amarillo+"|"+reset)
	print (amarillo+"		|"+reset+"       Creado por:"+verde+" Omar_Mendoza.   "+reset+amarillo+"|"+reset)
	print (amarillo+"		|"+reset+"             Version:"+rojo+" 1.0          "+reset+amarillo+"|"+reset)
	print (amarillo+"		-------------------------------------"+reset)
	print ("\n")
	pass
