from operaciones import *

a,b,c,d=(10,5,0,"Hola")
print("{}+{}={}".format(a, b, sumar(a, b)))
print("{}-{}={}".format(b, d, restar(a, b)))
print("{}*{}={}".format(b, b, producto(b, b)))
print("{}/{}={}".format(a, c, division(a, c)))
