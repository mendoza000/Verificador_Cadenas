from membrete import *

def clave():

	# ---Contadores---
	espacio    = 0
	caracter   = 0
	punto      = 0
	arroba     = 0
	barras     = 0
	especial   = 0
	numero     = 0
	incorrecto = 0
	# ----------------

	os.system("cls")
	titulo()
	cadena = input("Ingrese su contrase#a: ")

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
		if (i == "#" or i == "$" or i == "%" or i == "&" 
	   	 	or i == "(" or i == ")" or i == "{" or i == "}" or i == "+"
	    	or i == "*" or i == "<" or i == ">"):
			especial = especial +1
			pass
		if (i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or
	   		 i == "7" or i == "8" or i == "9" or i == "0"):
			numero = numero +1
			pass
		if (i == "!" or i == "¡" or i == "¿" or i == "?" or i == "="
	  		or i == "," or i == ";" or i == ":"):
			incorrecto = incorrecto +1
			pass

		caracter = caracter +1

	print(amarillo+"\n-----"+reset+rojo+"CONTRASE#A ANALIZADA"+reset+amarillo+"-----"+reset)
	print(f"\nSu contrase#a tiene... \n")

	print(f"Caracteres totales: {caracter}")
	print(f"Puntos: {punto}")
	print(f"Arrobas: {arroba}")
	print(f"Espacios: {espacio}")
	print(f"Barras: {barras}")
	print(f"Especiales: {especial}")
	print(f"Numeros: {numero}")
	print(f"Incorrectos: {incorrecto}\n")

	if (caracter == 8 and espacio == 0 and incorrecto == 0):
		print(naranja+"[-] "+reset+verde+"Su contrase#A cumple con los requisitos minimos."+reset)
		pass
	elif (caracter >= 8 and espacio == 0 and incorrecto == 0 and numero >= 1 or punto >=1 or arroba >= 1 or barras >= 1 or especial >= 1):
		print(naranja+"[=] "+reset+verde+"Su contrase#a se considera fuerte."+reset)
		pass
	else:
		print(naranja+"[!] "+reset+rojo+"Su contrase#a no cumple los requisitos minimos."+reset)
		pass

	os.system("pause")
	pass