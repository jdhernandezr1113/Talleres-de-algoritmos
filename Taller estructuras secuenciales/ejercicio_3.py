#entradas
sueldo=float(input("Escriba su sueldo: "))
v1=float(input("Escriba su primera venta: "))
v2=float(input("Escriba su segunda venta: "))
v3=float(input("Escriba su tercera venta: "))
#caja negra
comision=((v1+v2+v3)*(0.10))
sueldot=((comision)+(sueldo))
#salidas
print(f"Su comisión será: {comision} , Su sueldo total es: {sueldot}")