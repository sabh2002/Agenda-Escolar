from registrar_notas import notas as s, notas_proyecto as proyecto #Importando modulo para registrar notas
from leer_notas import leernotas as leer #Importando modulo para leer notas
from aprobadas_y_reprobadas import* #Importando modulo para ver materias aprobadas y reprobadas
from registrar_evaluaciones import* #Importando Modulo para Registrar evaluaciones
from eliminar_evaluaciones import* #Importando Modulo para eliminar evaluaciones

materias=("Matematica I","Algoritmica y Programacion","Acreditables","Proyecto Sociotecnologico I","Idiomas","Arquitectura del computador","Formacion Critica I","Electiva")
for i in range(len(materias)):
	try:
		materia=open(materias[i])# Para comprobar que los archivos existen
		materia.close()
	except FileNotFoundError:
		materia=open(materias[i],"w")# Si los archivos no existen crearlos desde 0
		for n in range(1,5):
			if materias[i]=="Proyecto Sociotecnologico I":
				materia.write("D"+"\t")
			else:
				materia.write("00"+"\t")
		materia.close()
	finally:
		materia=open(materias[i],"r+")# Para que la apertura de los archivos sea correcta
		materia.close()
def registrar_notas():# Para Registrar Notas
	while 1:# Menu Registro de notas
		
		print("----- Elige Materia a que quieres agregar o modificar notas: -----")
		print("")
		for i in range(len(materias)):
			print(str(i+1)+")",materias[i])
		print("0)Atras")
		try:
			op=input(">>>")
			op=int(op)
			if not op in range(0,9):
				print("El numero que usted ingreso no esta asignado a ninguna unidad curricular")
				input("presione cualquier tecla para continuar....")
		except ValueError:
			print("*Opcion Invalida!... Vuelve a intentarlo*\n")
			input("Presione cualquier tecla... Para continuar")
		if op==1:
			print("\t\tIngrese notas de |"+materias[0]+"|:\t\t")
			materia=open(materias[0],"r+")
			s(materia)
			materia.close()
			
			
		elif op==2:
			print("\t\tIngrese notas de |"+materias[1]+"|:\t\t")
			materia=open(materias[1],"r+")
			s(materia)
			materia.close()
		elif op==3:
			print("\t\tIngrese notas de |"+materias[2]+"|:\t\t")
			materia=open(materias[2],"r+")
			s(materia)
			materia.close()
		elif op==4:
			
			proyecto()



		elif op==5:
			print("\t\tIngrese notas de |"+materias[4]+"|:\t\t")
			materia=open(materias[4],"r+")
			s(materia)
			materia.close()
		elif op==6:
			print("\t\tIngrese notas de |"+materias[5]+"|:\t\t")
			materia=open(materias[5],"r+")
			s(materia)
			materia.close()
		elif op==7:
			print("\t\tIngrese notas de |"+materias[6]+"|:\t\t")
			materia=open(materias[6],"r+")
			s(materia)
			materia.close()
		elif op==8:
			print("\t\tIngrese notas de |"+materias[7]+"|:\t\t")
			materia=open(materias[7],"r+")
			s(materia)
			materia.close()
		elif op==0:

			break
		
		
def leer_notas():# Para leer notas
	while 1:# Menu Lectura de notas
		print("----- Eliga la materia de la cual desea consultar notas: -----")
		print("")
		for i in range(len(materias)):
			print(str(i+1)+")",materias[i])
		print("0)Atras")
		try:
			op=input(">>>")
			op=int(op)
		except ValueError:
			print("*Opcion Invalida!... Vuelve a intentarlo*\n")
		if op in range(1,9):
			print("")
			print("\t\t\t|"+materias[op-1]+"|:"+"\t\t")
			leer(materias[op-1])
			print("")
			input("presione cualquier tecla para continuar....")
			print("")
		elif op==0:
			break
		elif op not in range(1,9):
			print("El numero que usted ingreso no esta asignado a ninguna unidad curricular")
			input("presione cualquier tecla para continuar....")
def materias_aprobadas_reprobadas():
	apro_repro()
while 1:# MENU PRINCIPAL
	print("")
	print("""\t\t***** AGENDA ESCOLAR *****\t\t
1)Notas
2)Materias Aprobadas y Reprobadas
3)Evaluaciones
4)Restaurar: Notas, Evaluaciones o Todo
0)Salir""")
	opcion=input(">")
	print("")
	if opcion=="1":
		while 1:
			print("""\t***NOTAS***\t
1)Registrar notas
2)Leer Notas
0)Atras""")
			opcion=input(">")
			if opcion=="1":
				registrar_notas()
			elif opcion=="2":
				leer_notas()
			elif opcion=="0":
				break
			else:
				print("*Opcion Invalida!... Vuelve a intentarlo*\n")
	elif opcion=="2":
		print("\t***MATERIAS APROBADAS Y REPROBADAS***\t")
		materias_aprobadas_reprobadas()
	elif opcion=="3":
		while 1:
			print("""\t***EVALUACIONES***\t
1)Ingresar Evaluacion pendiente
2)Consultar Evaluaciones pendientes
3)Eliminar Evaluacion pendiente
0)Atras""")
			opcion=input(">")
			if opcion=="1":
				evaluacionespen()
			elif opcion=="2":
				leer=open("EVALUACIONES","r")
				l=leer.readlines()
				if  l==[]:
					print("\t\tNo Hay Evaluaciones pendientes!...")
					print("")
				for i in l:
					print(i)
				leer.close()
				input("Presione cualquier tecla para continuar...")
				print("")
			elif opcion=="3":
				print("")
				eliminar()
			elif opcion=="0":
				break
			else:
				print("*Opcion Invalida!... Vuelve a intentarlo*\n")
	elif opcion=="4":
		print("""QUE DESEAS ELIMINAR:
1)Todas las notas
2)Todas la Evaluaciones
3)TODO
-Presione Cualquier otra tecla para Salir""")
		opcion=input(">")
		if opcion=="1":
			print("Escribe CONFIRMAR para eliminar todas las Notas:")
			confirmar=input("")
			if confirmar=="CONFIRMAR":
				for i in range(len(materias)):
					materia=open(materias[i],"w")
					for n in range(1,5):
						if materias[i]=="Proyecto Sociotecnologico I":
							materia.write("F"+"\t")
						else:
							materia.write("00"+"\t")
				print("\n\t-----Se han eliminado todas las Notas exitosamente-----\n")
				input("Presiona Cualquier tecla para continuar...")
			else:
				print("\n\t-----Has cancelado ELIMINAR todas las Notas-----\n")
				input("Presiona Cualquier tecla para continuar...")

		elif opcion=="2":
			print("Escribe CONFIRMAR para eliminar todas las Evaluaciones:")
			confirmar=input("")
			if confirmar=="CONFIRMAR":
				eva=open("EVALUACIONES","w")
				print("\n\t-----Se han eliminado todas las Evaluaciones exitosamente-----\n")
				input("Presiona Cualquier tecla para continuar...")
			else:
				print("\n\t-----Has cancelado ELIMINAR todas las Evaluaciones-----\n")
				input("Presiona Cualquier tecla para continuar...")
		
		elif opcion=="3":
			print("Escribe CONFIRMAR para eliminar TODO")
			confirmar=input("")
			if confirmar=="CONFIRMAR":
				for i in range(len(materias)):
					materia=open(materias[i],"w")
					for n in range(1,5):
						if materias[i]=="Proyecto Sociotecnologico I":
							materia.write("F"+"\t")
						else:
							materia.write("00"+"\t")
				eva=open("EVALUACIONES","w")
				print("\n\t-----Se ha RESTAURADO el Programa de manera exitosa-----\n")
				input("Presiona Cualquier tecla para continuar...")
			else:
				print("\n\t-----Has cancelado la RESTAURACION del Programa-----\n")
				input("Presiona Cualquier tecla para continuar...")
		

	elif opcion=="0":
		break

	else:
		print("*Opcion Invalida!... Vuelve a intentarlo*\n")
