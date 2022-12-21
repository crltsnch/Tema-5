def sumar(a, b):
    return a+b
def restar(a, b):
    return a-b
def producto(a, b):
    return a*b
def division(a, b):
    return a/b

def errorZero(a, b):
    try:
        division
    except ZeroDivisionError:
        print("No es posible dividir entre cero")

def TypeError(a, b):
    try:
        a, b= int(a), int(b)
    except TypeError:
        print("No se puede sumar texto y un número")

