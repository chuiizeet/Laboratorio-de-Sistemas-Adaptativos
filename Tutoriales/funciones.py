'''
 Funciones
 
 Estructura.-
 
 def NOMBRE(PARAMETRO1, PARAMETRO2, ...):
	INSTRUCCIONES
	[return RESULTADO]
'''

#Ejemplos

#Funcion sin parametros
def imprime_hola():
	print('Hola')


#Funcion con parametros
def imprime_nombre(nombre):
	print('Hola, '+nombre)

#Funcion que recibe un parametro y regresa un valor
def convierte_a_binario(valor_decimal):
	binario=bin(valor_decimal)[2:]
	return binario
#Aqui llamamos a las funciones

imprime_hola()
imprime_nombre('Pedro')
imprime_nombre('Juan')
binario2=convierte_a_binario(2)
binario10=convierte_a_binario(10)
binario20=convierte_a_binario(20)

print('Los valores binarios para 2, 10 y 20 son respectivamente '+binario2+', '+binario10+' y '+binario20)