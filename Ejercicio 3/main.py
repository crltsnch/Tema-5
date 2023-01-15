from gestor import *

if __name__ == "__main__":
    g = Gestor()
    g.añadir(Personaje('Caballero', 4, 2, 4, 2))
    g.añadir(Personaje('Guerrero', 2, 4, 2, 4))
    g.añadir(Personaje('Arquero', 2, 4, 1, 8))
    g.mostrar()
    g.borrar('Arquero')
    g.mostrar()