a = input("Ingrese un número: ")
b = input("Ingrese otro número: ")

def sumar():
    return a+b
def restar():
    return a-b
def producto():
    return a*b
def division():
    resultado=a/b
    try:
        b=0
    except ZeroDivisionError:
        print("No es posible dividir entre cero")
    return resultado
try:
    a=str
    b=str
except TypeError:
    print("No se puede sumar texto y un número")

