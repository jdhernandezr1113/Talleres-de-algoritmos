#entrada
presupuesto=float(input("Digite el monto para el presupuesto del hospital"))
#caja negra
gine=(presupuesto*0.40)/100
trauma=(presupuesto*0.30)/100
pedia=(presupuesto*0.30)/100
#salida
print(f"El presupuesto para el area de ginecología es de: {gine} , para traumatología es de: {trauma} , para pediatría es de {pedia}")