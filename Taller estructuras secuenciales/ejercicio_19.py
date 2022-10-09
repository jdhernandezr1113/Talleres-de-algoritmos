#entrada
n=int(input("Cantidad de naranjas compradas: "))
r=float(input("Precio al que vende la docena: "))
k=float(input("Venta total: "))
#caja negra
v=(n/12)*r
v_t=(((k-r)*100)/v)
#salidas
print(f"La ganancia fue de {v_t} %")