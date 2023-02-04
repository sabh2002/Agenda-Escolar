def notas(materia):# El parametro "materia", es donde seran almacenadas las notas
				   #(materia sera el archivo de texto)

	"""Este modulo esta encargado de registrar
	las cuatro notas de una unidad curricular en un archivo de texto"""
	print("")			
	for i in range(1,5):
		print("")
		print("""Elige a cual Unidad le quieres Agregar o Modificar una Nota, 0 para Salir
1)Unidad I
2)Unidad II
3)Unidad III
4)Unidad IV
0)Atras""")
		nota=input(">>>")
		print("")
		if nota=="1": #Para Registrar o Modificar nota I
			nota1=input("-Ingrese nota I: ")
			while len(nota1)!=2 or not nota1.isnumeric():
				print("")
				print("*ERROR:")
				if len(nota1)!=2:
					print("-La nota debe contener 2 digitos")
				if not nota1.isnumeric():
					print("-La nota debe ser numerica")
				print(" ")
				nota1=input("-Ingrese nota I: ")
			materia.seek(0)
			materia.write(str(nota1)+"\t")

		elif nota=="2": #Para Registrar o Modificar nota II
			nota2=input("-Ingrese nota II: ")
			while len(nota2)!=2 or not nota2.isnumeric():
				print("")
				print("*ERROR:")
				if len(nota2)!=2:
					print("-La nota debe contener 2 digitos")
				if not nota2.isnumeric():
					print("-La nota debe ser numerica")
				print(" ")
				nota2=input("-Ingrese nota II: ")
			materia.seek(3)
			materia.write(str(nota2)+"\t")

		elif nota=="3": #Para Registrar o Modificar nota III
			nota3=input("-Ingrese nota III: ")
			while len(nota3)!=2 or not nota3.isnumeric():
				print("")
				print("*ERROR:")
				if len(nota3)!=2:
					print("-La nota debe contener 2 digitos")
				if not nota3.isnumeric():
					print("-La nota debe ser numerica")
				print(" ")
				nota3=input("-Ingrese nota III: ")
			materia.seek(6)
			materia.write(str(nota3)+"\t")

		elif nota=="4": #Para Registrar o Modificar nota IV
			nota4=input("-Ingrese nota IV: ")
			while len(nota4)!=2 or not nota4.isnumeric():
				print("")
				print("*ERROR:")
				if len(nota4)!=2:
					print("-La nota debe contener 2 digitos")
				if not nota4.isnumeric():
					print("-La nota debe ser numerica")
				print(" ")
				nota4=input("-Ingrese nota IV: ")
			materia.seek(9)
			materia.write(str(nota4)+"\t")
		elif nota=="0":
			break

			
		else: #Para finalizar registro de notas
			
			print("*Opcion Invalida... Vuelve a intentarlo")
	"""
	Las siguientes lineas calculan el valor acumulado y el promedio total"""
	total=materia 
	total.seek(0)
	notas=total.read()
	n1=notas[0]+notas[1]
	n2=notas[3]+notas[4]
	n3=notas[6]+notas[7]
	n4=notas[9]+notas[10]
	acumulado=int(n1)+int(n2)+int(n3)+int(n4)
	promedio=((acumulado/4)*20)/25

	promedio="{0:.2f}".format(promedio)
	if float(promedio)<10:
		promedio="0"+str(promedio)
	nota=materia
	if acumulado==None:
		acumulado=00
	nota.seek(12)

	nota.write("\t"+str(acumulado)+"\t\t"+str(promedio))
	nota.seek(0)
	nota.close()
def notas_proyecto():
	print("\t\tIngrese notas de |Proyecto Sociotecnologico I|:\t\t")
	materia=open("Proyecto Sociotecnologico I","r+")
	print("")
	for i in range(1,5):
		print("""Elige a cual Unidad le quieres Agregar o Modificar una Nota, 0 para Salir
1)Unidad I
2)Unidad II
3)Unidad III
4)Unidad IV
0)Atras""")
		nota=(int(input(">>>")))
		print("")
		excepcion=["1","2","3","4","5","6","7","8","9","0"]
		aceptadas=["A","B","C","D"]
		if nota==0:
			break
		if nota==1: #Para Registrar o Modificar nota I
			nota1=input("-Ingrese nota I: ")
			while len(nota1)!=1 or nota1 in excepcion or not nota1.upper() in aceptadas:
				print("Las notas del Proyecto Sociotecnologico se evaluan con letras de la A a la D... Vuelve a intentarlo: ")
				print(" ")
				nota1=input("-Ingrese nota I: ")
			materia.seek(0)
			materia.write(str(nota1.upper())+"\t")
			
		elif nota==2: #Para Registrar o Modificar nota II
			nota2=input("-Ingrese nota II: ")
			while len(nota2)!=1 or nota2 in excepcion or not nota2.upper() in aceptadas:
				print("Las notas del Proyecto Sociotecnologico se evaluan con letras de la A a la D... Vuelve a intentarlo: ")
				print(" ")
				nota2=input("-Ingrese nota II: ")
			materia.seek(2)
			materia.write(str(nota2.upper())+"\t")

			

		elif nota==3: #Para Registrar o Modificar nota III
			nota3=input("-Ingrese nota III: ")
			while len(nota3)!=1 or nota3 in excepcion or not nota3.upper() in aceptadas:
				print("Las notas del Proyecto Sociotecnologico se evaluan con letras de la A a la D... Vuelve a intentarlo: ")
				print(" ")
				nota3=input("-Ingrese nota III: ")
			materia.seek(4)
			materia.write(str(nota3.upper())+"\t")
	
		elif nota==4: #Para Registrar o Modificar nota IV
			nota4=input("-Ingrese nota IV: ")
			while len(nota4)!=1 or nota4 in excepcion or not nota4.upper() in aceptadas:
				print("Las notas del Proyecto Sociotecnologico se evaluan con letras de la A a la D... Vuelve a intentarlo: ")
				print(" ")
				nota4=input("-Ingrese nota IV: ")
			materia.seek(6)
			materia.write(str(nota4.upper())+"\t")
		elif not nota in range(1,5):
			print("*Opcion Invalida... Vuelve a intentarlo")
		
	materia.close()
		