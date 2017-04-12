hours =1
import numpy as np
#constantes
a1 = 20

a2 = 20

g1 = 1/30.0

g2 = 1/30.0

const = {'g1': '1/30.0', 'a2': '20', 'a1': '20', 'g2': '1/30.0'}
#valores iniciales
initVals = [0.0, 0.0]
#parametros en el diccionario
params = {'p1': 'xs[0]', 'p2': 'xs[1]'}
#parametros en el diccionario reversados
revparams = {'xs[0]': 'p1', 'xs[1]': 'p2'}
#ecuaciones diferenciales
def p1(xs,const,t):
	return +a1   -g1*xs[0] 
def p2(xs,const,t):
	return +a2   -g2*xs[1] 
#arreglo de funciones
funcArray = [p1, p2]
#acciones
actions = [[60.0, 0.0], [-1.0, 0.0], [0.0, 60.0], [0.0, -1.0]]
#eventos
def darEventos(xs):
	return [a1,g1*xs[0],a2,g2*xs[1]]
