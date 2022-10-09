#entradas
bolivar=float(input("Ingrese la cantidad de bolivares: "))
bolivard=float(input("Ingrese la cantidad de bolivares después del impuesto: "))
#caja negra
razon=(bolivard/bolivar)
impuesto=(razon*4*bolivar)/100
#salida
print(f"El total de impuesto cobrado fue de: {impuesto}")