#entrada
costo_k=float(input("Insertar valor por kilovatio: "))
lec_ant=float(input("Ingresar lectura anterior de consumo: "))
lec_act=float(input("Ingresar lectura acutal de consumo: "))
#caja negra
pago_luz=((lec_act-lec_ant)*(costo_k))
#salida
print("El valor a pagar del recibo de la luz es:"+str(pago_luz))