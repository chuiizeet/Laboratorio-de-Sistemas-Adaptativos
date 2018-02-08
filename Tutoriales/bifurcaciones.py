'''
 Bifurcaciones

 Estructura.-

 if CONDICION:
     INSTRUCCIONES
 [elif CONDICION:
     INSTRUCCIONES
  else:
     INSTRUCCIONES
  ]

  **Las palabras en mayusculas indican estatutos variables (no siempre son los mismos)
  y lo que esta en corchetes es opcional. Puede haber mas de un elif.
'''

#Ejemplos
matricula=20
temperatura=40

if matricula%2==0:
    print('La matricula es par')
else:
    print('La matricula es impar')


if temperatura<15:
          print('Tengo frio')
elif temperatura>=15 and temperatura<26:
          print('Esta agradable')
elif temperatura>=26 and temperatura<35:
          print('Tengo calor')
else:
          print('Tengo mucho calor')
