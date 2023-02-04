def apro_repro():
	"""Este modulo agrega a una lista las materias aprobadas y reprobadas respectivamente,
	 y luego las imprime por pantalla """
	materias=("Matematica I","Algoritmica y Programacion","Acreditables","Idiomas","Arquitectura del computador","Formacion Critica I","Electiva")
	aprobadas=[]
	reprobadas=[]
	for acumulado in range(len(materias)):
		try:
			a_r=open(materias[acumulado-1],"r+")
			a_r.seek(17)
			d=a_r.read()
			valor=d[0]+d[1]+d[2]+d[3]+d[4]
			valor=float(valor)
			
		except IndexError:
			print("*Tienes",'"'+materias[acumulado-1]+'"',"sin ninguna nota")
			continue
		if valor>=10:
			aprobadas.append(materias[acumulado-1])
	
		if valor<10 or valor==None:
			reprobadas.append(materias[acumulado-1])
	print("")
	print("\t\tAPROBADAS:\t\t")
	print("")
	for materia in aprobadas:
		print("-",materia)
	print("")
	print("\t\tREPROBADAS:\t\t")
	print("")
	for materia in reprobadas:
		print("-"+materia)
	print("")
	input("Presione cualquier tecla para continuar....")