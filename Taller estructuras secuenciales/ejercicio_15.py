#entradas
pvp=float(input("Precio de venta al publico: "))
pfp=float(input("Precio de compra final: "))
#caja negra
d=(pvp-pfp)
desc=round(((d/pvp)*100),3)
#salida
print(f"El descuento que se aplico al precio de venta es: {desc} %")