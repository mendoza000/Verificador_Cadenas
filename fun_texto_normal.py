from title import *

def texto_normal():

	# ---Contadores---
	espacio  = 0
	caracter = 0
	punto    = 0
	arroba   = 0
	barras   = 0
	especial = 0
	numero   = 0
	# ----------------

	os.system("cls")
	titulo()
	cadena = input("\nIngrese su texto: ")

	for i in cadena:

		if (i == " "):
			espacio = espacio +1
			pass
		if (i == "."):
			punto = punto +1
			pass
		if (i == "@"):
			arroba = arroba +1
			pass
		if (i == "-" or i == "_" or i == "/"):
			barras = barras +1
			pass
		if (i == "!" or i == "#" or i == "$" or i == "%" or i == "&" 
	   	 	or i == "(" or i == ")" or i == "{" or i == "}" or i == "+"
	    	or i == "*" or i == "¡" or i == "¿" or i == "?" or i == "="
	  		or i == "<" or i == ">" or i == "," or i == ";" or i == ":"):
			especial = especial +1
			pass
		if (i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or
	   		 i == "7" or i == "8" or i == "9" or i == "0"):
			numero = numero +1
			pass

		caracter = caracter +1

	print(am+"\n-----"+re+ro+"TEXTO ANALIZADO"+re+am+"-----"+re)
	print(f"\nSu texto tiene... \n")

	print(f"Caracteres totales: {caracter}")
	print(f"Puntos: {punto}")
	print(f"Arrobas: {arroba}")
	print(f"Espacios: {espacio}")
	print(f"Barras: {barras}")
	print(f"Especiales: {especial}")
	print(f"Numeros: {numero}")

	os.system("pause")
	pass