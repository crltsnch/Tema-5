from io import open
import pickle

class Personaje:
    def __init__(self, nombre, propiedades, ataque, defensa, alcance):
        self.nombre = nombre
        self.propiedades = propiedades
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
    
    def __str__(self):
        return '{} => Propiedades: {} Ataque: {} Defensa: {} Alcance: {}'.format(self.nombre, self.propiedades, self.ataque, self.defensa, self.alcance)

    
class Gestor:
    personajes = []

    def __init__(self):
        self.cargar()

    def añadir(self, p):
        for personaje in self.personajes:
            if personaje.nombre == p.nombre:
                return
        self.personajes.append(p)
        self.guardar()
    
    def borrar(self, nombre):
        for personaje in self.personajes:
            if personaje.nombre == nombre:
                self.personajes.remove(personaje)
                self.guardar()
                print('Personaje {} borrado correctamente'.format(nombre))
                return
        print('No se ha encontrado el personaje {}'. format(nombre))

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