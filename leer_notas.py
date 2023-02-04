def leernotas(materia):# El parametro "materia", es donde seran almacenadas las notas
				   #(materia sera el archivo de texto)
	"""Este modulo se encarga de mostrar las notas de cada materia, lo acumulado y el promedio"""
	nota=open(materia,"r+")
	print("I\tII\tIII\tIV\t\tAcumulado:\tPromedio")
	
	print(nota.read())
	nota.close()