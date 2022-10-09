#Entradas
import math
a=float(input("Ingrese lado A: "))#float
b=float(input("Ingrese lado B: "))#float
c=float(input("Ingrese lado C: "))#float
#CajaNegra
s=(a+b+c)/2#float
area=math.sqrt(s*(s-a)*(s-b)*(s-c))#float
#Salidas
print("El area del triangulo es: "+str(area))#str