'''
 Listas

Vamos a ejemplificar algunas de las funciones/metodos para listas, sobre todo las que vamos a utilizar.
Supongamos que tenemos una lista, llamada mi_lista

Puedes encontrar mas informacion sobre listas en: https://docs.python.org/3/tutorial/datastructures.html

'''

#Inicializacion de una lista vacia
mi_lista=[]

#Para agregar elementos a la lista (nota que tambien podemos hacer esto con un ciclo)
mi_lista.append(1)
mi_lista.append(2)
mi_lista.append(3)
mi_lista.append(4)

#Declaracion de una lista con varios elementos
lista2=['a','b','c','d','e','f','g']

#len nos da la cantidad de elementos que hay en la lista
longitud=len(mi_lista)
print('Hay '+str(longitud)+' elementos en la lista.')

#Para recorrer la lista con un for-each
suma=0
for elemento in mi_lista:
    suma=suma+elemento
print(suma)

#Para recorrer la lista con los elementos indizados
for i in range(len(mi_lista)-1):
    if(mi_lista[i]>mi_lista[i+1]):
        mayor=mi_lista[i]
    else:
        mayor=mi_lista[i+1]
print(mayor)

#Como arriba se menciona, se pueden seleccionar elementos especificos de la lista. Ejemplo:
print('Primer elemento de la lista: '+str(mi_lista[0]))
    
#El metodo pop() devuelve el ultimo elemento de la lista y lo quita de la misma
print('Hagamos pop()')
ultimo=mi_lista.pop()
print(ultimo)
print(len(mi_lista))

print('Hagamos pop()')
ultimo=mi_lista.pop()
print(ultimo)
print(len(mi_lista))
