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
        for p in self.personajes:
            print(p)
    
    def cargar(self):
        fichero = open('personajes.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            print('fichero vacío')
        finally:
            fichero.close()
    
    def guardar(self):
        fichero = open('personajes.pckl', 'wb')
        pickle.dump(self.persoanajes, fichero)
        fichero.close()