Algoritmo inicio_primera_letra
	//entradas
	Escribir "Nombre"
	Leer nombre
	Escribir "Primer Apellido"
	Leer primer_apellido
	Escribir "Segundo Apellido"
	Leer segundo_apellido
	//caja negra
	m<-Subcadena(nombre,1,1)
	pa<-Subcadena(primer_apellido,1,1)
	sa<-Subcadena(segundo_apellido,1,1)
	//Salida
	Escribir m pa sa
	
FinAlgoritmo
