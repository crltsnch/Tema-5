import sys

def main():
    fichero = open('contador.txt')
    contenido = fichero.readline()

    if len(contenido)== 0:
        contenido=0
    
