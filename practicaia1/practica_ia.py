import sys
import random
matris_x=[]
tetas=[]
vector_y=[]
archivo_x="hola"
archivo_y="hola"
alfa=0.001
m=0 #numeros de datos
n=0 #numero de variables x
itera=10 #numero de iteraciones
tole=0.02 #tolerancia dada
def main():
	global m
	global n
	global matris_x
	global archivo_x
	global archivo_y
	global alfa
	global tole
	global itera
	global vector_y
	print  "PRACTICA INTELIGENCIA ARTIFICIAL I" 
    #lee si se mandaron parametros
	if len(sys.argv) >= 6:
		archivo_x=sys.argv[1]
		archivo_y=sys.argv[2]
		alfa=float(sys.argv[3])
		itera=int(sys.argv[4])
		tole=float(sys.argv[5])

	else:
		print  "No se introdujo parametros o falto parametros" 
		print  "Ingreselos a continuacion:"
		archivo_x=raw_input("Archivo de entrada de var x: ")
		archivo_y=raw_input("Archivo de entrada de var y: ")
		alfa  =  float(input("Ingrese numero alfa: "))
		itera =  int(  input("Ingrese el maximo de interaciones: "))
		tole=    float(input("Ingrese la tolerancia:"))
	print  "_______________________________________________________" 
	print  "El analisis se realizara con los siguientes parametros" 
	print  "Archivo var x:",archivo_x," Archivo var y:",archivo_y
	print "Alfa: ",alfa," Iteracione: ",itera," Tolerancia: ",tole
	print  "_______________________________________________________" 
	
	leer_x (archivo_x)
	leer_y (archivo_y)
	init_tetas()
	gradiente()
	imprime_teta()
	
def imprime_teta():
	global tetas
	teta=0
	tam=len(tetas)
	while teta<tam:
		print "Teta",teta,"=",tetas[teta]
		teta=teta+1

def leer_x(archivo):
	 global m
	 global n
	 global matris_x
	 archi=open(archivo,'r')
	 linea=archi.readline()
	 while linea!="": 
	 
		 vector=linea.split(',',2)
		
		 n=len(vector)
		 m=m+1
		 i=0
		 #convertir vector de texto a float
		 vectoraux=[]
		 vectoraux.append(1.00)
		 while i<n:
			vectoraux.append(float(vector[i]))
			i=i+1
		 matris_x.append(vectoraux)
		 n=len(vector)+1
		 linea=archi.readline()
	 print "m=",m," n=",n
	 
def init_tetas():
		global n
		global tetas
		i=0
		while i<n:
			tetas.append(random.uniform(1, 2))
			i=i+1
			
def leer_y(archivo):
	 global m
	 global vector_y
	 m=0
	 vector_y=[]
	 archi=open(archivo,'r')
	 linea=archi.readline()
	 while linea!="": 
		 m=m+1
		 num=float(linea)
		 vector_y.append(num)
		 linea=archi.readline()
	 print "m=",m," n=",n
	 
def h(i):
	global matris_x
	global tetas
	vector_x=matris_x[i]
	tamanio=len(vector_x)
	suma=0
	j=0
	val_teta=1
	while j<tamanio:
		val_teta=tetas[j]
		presuma=vector_x[j]*val_teta
		suma=suma+presuma
		j=j+1
	return suma
	
def x(i):
	global matris_x
	vector_x=matris_x[i]
	tamanio=len(vector_x)
	suma=0
	j=0

	while j<tamanio:
		suma=suma+vector_x[j]
		j=j+1
	return suma
def dj_dTJ(teta,xi):
		global matris_x
		global vector_y
		global m
		fila=0
		uno_m=1/m
		i=0
		suma=0
		while i<m:
			yval=vector_y[i]
			val_h=h(i)
			val_xi=xi
			pre_val=val_h-yval
			pre_val=pre_val*val_xi
			suma=suma+pre_val
			i=i+1
		suma=suma*uno_m
		return suma
def gradiente():
	global alfa
	global itera
	global tole
	global tetas
	global n
	global alfa 
	teta=0
	cont_teta=0
	cont=0
	while cont<itera:
		while cont_teta<n:
			teta=tetas[cont_teta]
			teta=teta-alfa *dj_dTJ(cont_teta,x(cont_teta))
			tetas[cont_teta]=teta
			cont_teta=cont_teta+1
		cont=cont+1
if __name__ == '__main__':
    main()
