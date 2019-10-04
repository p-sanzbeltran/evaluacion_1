#En este programa le pedimos al usuario
#que teclee los coeficientes del polinomio
#y hallamos el valor de las raices
import math
def ecuacion():
    print"teniendo en cuenta la ecuacion ax^2+bx+c"
    print"----------------------------------------"
	
    a=input("Introduce el valor de a: ")
    b=input("Introduce el valor de b: ")
    c=input("Introduce el valor de c: ")
    d=(b*b-4*a*c)

    if (d<0):
        print"La ecuacion no tiene soluciones reales"
    else:
        raiz1=(-b+math.sqrt(d))/(2*a)
        raiz2=(-b-math.sqrt(d))/(2*a)
	
        print"primera solucion= " , raiz1
        print"segunda solucion= " , raiz2
	
ecuacion()
