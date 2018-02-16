import sys


cesar3={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j','h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q','o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x','v':'y','w':'z','x':'a','y':'b','z':'c'}
letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cesardinamico={}

def crearDiccionario():
    desfase = int(sys.argv[2])-1
    index = 0
    for letra in letras:
        indice = index+desfase
        if(indice > len(letras)-desfase):
            indice = desfase+1 - (len(letras)-index)
        cesardinamico[letra] = letras[indice]
        index +=1

def nombreDinamico(tokens):
    cifrado=''
    for token in tokens:
            for char in token:
                for key in cesardinamico.keys():
                    if(char == key):
                        cifrado += cesardinamico[key]
            cifrado += " "
    return cifrado

def nombreCesar(tokens):
    cifrado=''
    for token in tokens:
            for char in token:  
                for key in cesar3.keys():
                    if(char == key):
                        cifrado += cesar3[key]
            cifrado += " "
    return cifrado

def printCifrado():
    for key in cesar3.keys():
        print("Letra: "+key+" Letra cifrada: "+cesar3[key])

def printRfc(tokens):
    Curp = tokens[len(tokens)-2][0:2]
    Curp += tokens[len(tokens)-1][0]
    Curp += tokens[0][0]
    print('Codigo para CURP o RFC: '+Curp.upper())
#Main
def main():
    try:
        archivo = open(sys.argv[1])
        lineas = archivo.readlines()
        nombre = lineas[0]
        tokens = nombre.split()
        cifradodinamico=''
        print('Nombre: '+nombre)
        cifrado = nombreCesar(tokens)
        print('Cifrado: '+cifrado)
        if(len(sys.argv) < 3):
            cifradodinamico="No se ingreso el parametro de desfase"
        else:
            crearDiccionario()
            cifradodinamico = nombreDinamico(tokens)
        print('Cifrado dinamico: '+cifradodinamico)
        printRfc(tokens)
        printCifrado()
        archivo.close()
    except IOError:
        print('No se puede abrir el arhivo')
        sys.exit(1)

main()