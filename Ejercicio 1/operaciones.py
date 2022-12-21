def sumar(a, b):
    try:
        a= int(a) or float(a)
        b= int(b) or float(b)
        return a+b
    except ValueError:
        print("Error: Tipo de dato no válido")

def restar(a, b):
    try:
        a= int(a) or float(a)
        b= int(b) or float(b)
        return a-b
    except ValueError:
        print("Error: Tipo de dato no válido")

def producto(a, b):
    try:
        a= int(a) or float(a)
        b= int(b) or float(b)
        return a*b
    except ValueError:
        print("Error: Tipo de dato no válido")

def division(a, b):
    try:
        a= int(a) or float(a)
        b= int(b) or float(b)
        return a/b
    except ValueError:
        print("Error: Tipo de dato no válido")
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero")

