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
	print matris_x
	print vector_y

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
		 while i<n:
			vectoraux.append(float(vector[i]))
			i=i+1
		 matris_x.append(vectoraux)
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
 
def dj_dTJ():
		global matris_x
		global vector_y
		global m
		fila=0
		
		uno_m=1/m
		i=0
		while i<m
			yval=vector_y[i]
			
		
if __name__ == '__main__':
    main()
