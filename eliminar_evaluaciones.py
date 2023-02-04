def eliminar():
	"""Este modulo fue creado para eliminar evaluaciones pendientes que han sido realizadas"""
	archivo=open("EVALUACIONES","r+")
	evaluaciones=archivo.readlines()
	cont=0
	contador=0
	indice=len(evaluaciones)-1
	while contador <= indice:
		l=evaluaciones[contador]
		print(str(contador+1)+")",l)
		contador+=1 
	print("---Seleccione la evaluacion que desea eliminar (0 para salir):")
	eva=open("EVALUACIONES","r+")
	rango=len(evaluaciones)
	
		
	archivo.close()
			
		
	
	while 1:
		try:
			delete=int(input(">"))
		
			if delete==0:
				break
			if delete <= rango:
				eva=open("EVALUACIONES","w")
				for linea in evaluaciones:

					if linea!=evaluaciones[delete-1]:
						eva.writelines(linea)
				break
			else:
			
				print("*Opcion Invalida vuelve a intentarlo\n")
		except ValueError:
			print("*Opcion Invalida vuelve a intentarlo\n")
			
			
			
		
	eva.close()



		

