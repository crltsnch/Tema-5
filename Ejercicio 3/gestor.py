from io import open
from logging.config import _RootLoggerConfiguration
import pickle

class Personaje:
    def __init__(self, nombre, propiedades, ataque, defensa, alcance):
        self.nombre = nombre
        self.propiedades = propiedades
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
    
class Gestor:
    personajes = []

    def añadir(self, p):
        for personaje in self.personajes:
            if personaje.nombre == p.nombre:
                return
        self.personajes.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.persoanjes) == 0:
            print('No hay personajes, el fichero esá vacio')
            return

