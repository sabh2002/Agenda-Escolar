def evaluacionespen():
	""" Este modulo esta encargado de registrar nuevas evaluaciones pendientes"""
	dia=input("Dia: ")
	mes=input("Mes: ")
	fecha=(dia+"/"+mes)
	evaluacion=input("Evaluacion: ")
	while len(evaluacion)>36:
		print("El nombre de la 'Evaluacion' es muy largo... Por favor vuelve a intentarlo")
		evaluacion=input("Evaluacion: ")
	tipo=input("Tipo: ")
	while len(tipo)>19:
		print("El nombre del 'Tipo de Evaluacion' es muy largo... Por favor vuelve a intentarlo")
		tipo=input("Tipo: ")
	valor=input("Valor: ")
	while len(valor)>2:
		print("El valor no puede contener mas de 2 digitos")
		valor=input("Valor: ")
	if not valor in "%":
		valor+="%"
	eva=open("EVALUACIONES","a+")
	eva.writelines("|Titulo: " + evaluacion + "    " + "|Tipo: " + tipo + "    " + "|Valor: " + valor + "    " + "|Fecha: " + fecha  + "\n")
	eva.close()


