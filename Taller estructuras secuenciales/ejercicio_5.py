#entrada
p1=float(input("ingrese nota del parcial 1: "))
p2=float(input("ingrese nota del parcial 2: "))
p3=float(input("ingrese nota del parcial 3: "))
e1=float(input("ingrese nota del examen final: "))
t1=float(input("ingrese nota del trabajo final: "))
#caja negra
N_f=((((p1+p2+p3)/3)*0.55)+(e1*0.30)+(t1*0.15))
#salida
print("La nota final es de: "+str(N_f))