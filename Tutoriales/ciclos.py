'''
 Ciclos

 For

 Estructura.-

 for VARIABLE in range(SECUENCIA):
     INSTRUCCIONES

 For each

 Estructura.-

 for VARIABLE in LISTA:
    INSTRUCCIONES

 While

 Estructura.-

 while CONDICION:
    INSTRUCCIONES
 
  **Las palabras en mayusculas indican estatutos variables (no siempre son los mismos).
'''

#Ejemplos

#Una lista con algunos personajes de la pelicula "Matrix"
lamatrix=['neo','felicity','morpheus','oraculo']

#Imprimir numeros 1-10
for j in range(1,11):
    print(j)

print()

#Imprimir numeros 0-9 (nota que el primer valor de range por default es 0)
for i in range(10):
    print(i)

print()

#Imprimir personajes de la lista lamatrix
for personaje in lamatrix:
    print(personaje)

#Otra manera de hacer la impresion de la lista lamatrix con ciclos
for i in range(len(lamatrix)):
    print("Personaje " + str(i) + ": " + lamatrix[i])
