'''
 Strings (cadenas de texto)

Vamos a ejemplificar algunas de las funciones/metodos para strings, sobre todo las que vamos a utilizar.
Los strings en Python son muy "amigables", ya que basicamente se tratan como listas.

Mas informacion sobre strings: https://docs.python.org/3/library/stdtypes.html

'''

h="hola"
m="mundo"
s="adios mundo cruel"

#Concatenacion de strings (se usa el +)
hola_mundo=h+", "+m
print(hola_mundo)

#Quebrar strings utilizando un separador (esta operacion produce una lista)
#Si el metodo .split() no recibe parametros, toma como separador el espacio en blanco,
#de otra manera, toma como separador el caracter que se le indique
tokens=s.split()

for token in tokens:
	print("Elemento de s:"+token)

#Un string en si tambien se puede ver como una lista
for caracter in h:
	print("Caracteres en el string h: "+caracter)

#El metodo len, al igual que con listas, nos devuelve la longitud de un string
print(len(m))

#Slicing nos permite, al igual que con listas, obtener partes de un string
print(s[0])
print(s[2:])
print(s[2:6])
print(s[2:10])
print(s[:5])