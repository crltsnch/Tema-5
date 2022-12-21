def sumar(a, b):
    try:
        return a+b
    except ValueError:
        print("Error: Tipo de dato no válido")

def restar(a, b):
    try:
        return a-b
    except ValueError:
        print("Error: Tipo de dato no válido")

def producto(a, b):
    try:
        return a*b
    except ValueError:
        print("Error: Tipo de dato no válido")
        
def division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")


