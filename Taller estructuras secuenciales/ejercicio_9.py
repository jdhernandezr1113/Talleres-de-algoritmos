#entradas
sueldobase=float(input("Escriba su sueldo base: "))
preciohoras=float(input("Escriba el precio por hora trabajada: "))
horas=int(input("Escriba las horas trabajadas: "))
#caja negra
salariototal=(((sueldobase)-(sueldobase*0.20))+(preciohoras*horas))
#salida
print(f"El salario total del trabajador es de: {salariototal}")