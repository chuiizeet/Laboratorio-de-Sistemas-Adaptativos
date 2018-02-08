'''
 Diccionarios

Vamos a ejemplificar algunas de las funciones/metodos mas comunes para un diccionario.
Supongamos que tenemos un diccionario, al cual llamaremos mi_dict

Puedes encontrar mas informacion sobre diccionarios en: https://docs.python.org/3/tutorial/datastructures.html

'''

#Inicializacion de un diccionario vacio
mi_dict={}

#Los diccionarios son estructuras que contienen pares en la forma llave:valor
#OJO: Las llaves son unicas. Por tanto, NO deben repetirse.

#Inicialicemos un diccionario llamado dict2 con algunos pares, donde las llaves son matriculas y los valores son nombres de alumnos
dict2={1234:'fulano',5678:'sutano',4567:'perengano'}

#Los diccionarios son muy eficientes para acceder informacion, pues la unicidad de la llave genera accesos de manera rapida (esto lo podemos constatar si estudiamos tablas de hash). En Python, podemos acceder a un valor dada una llave de la siguiente manera (ejemplo con dict2):

valor=dict2[1234]
print('Alumno con matricula ' + str(1234) + ': ' + valor)

#Tambien podemos recorrer diccionarios
for key in dict2.keys():
    print('Matricula: '+str(key)+' Nombre: '+dict2[key])

#De igual manera, es posible agregar nuevos valores a un diccionario. Por ejemplo, supongamos que queremos agregar telefonos en mi_dict
mi_dict['amiguito']='81 12 34 56'
print('Telefono de amiguito: '+mi_dict['amiguito'])

#Si una llave ya existe dentro del diccionario y le asignamos un valor, el valor anterior se sobreescribe:
mi_dict['amiguito']='81 77 77 77'
print('Nuevo telefono de amiguito: '+mi_dict['amiguito'])

#Es por eso que tenemos metodos para verificar la existencia de una llave en el diccionario:
if 'amiguito' in mi_dict.keys():
    print('Amiguito ya esta en la agenda')
else:
    print('Amiguito no esta en la agenda')
