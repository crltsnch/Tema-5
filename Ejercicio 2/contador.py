import sys

def main():
    fichero = open('contador.txt', 'a+')
    contenido = fichero.readline()

    if len(contenido) == 0:
        contenido = '0'
        fichero.write(contenido)
    fichero.close()

    try:
        contador = int(contenido)
        if len(sys.argv) == 2:
            if sys.argv[1] == 'inc':
                contador =+ 1
            elif sys.argv[1] == 'dec':
                contador -= 1
        print(contador)
        fichero = open('contador.txt', 'w')
        fichero.write(str(contador))
        fichero.close()
    except ValueError:
        print('Error: Fichero corrupto')