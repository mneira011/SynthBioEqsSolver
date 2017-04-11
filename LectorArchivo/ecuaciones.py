import numpy as np
#constantes
a = 0

b=3

c=5

const = {'a': 0.0, 'b': 3.0, 'c': 5.0}
#valores iniciales
initVals = [3.0, 4.0, 2.0]
#parametros en el diccionario
params = {'y': 'xs[1]', 'z': 'xs[2]', 'x': 'xs[0]'}
#parametros en el diccionario reversados
revparams = {'xs[1]': 'y', 'xs[0]': 'x', 'xs[2]': 'z'}
#ecuaciones diferenciales
def x(xs,const,t):
	return -3*xs[0]*4*xs[1]   +a  +1/b 
def y(xs,const,t):
	return -3*xs[1]*4*xs[0]   -1/b 
def z(xs,const,t):
	return -1/b 
#arreglo de funciones
funcArray = [y, z, x]
#acciones
actions = [[1.0, 0.0, 0.0], [0.0, 0.0, 0.0], [-1.0, -2.0, -3.0], [0.0, 2.0, 0.0]]
#eventos
def darEventos(xs):
	return [3*xs[0]*4*xs[1],a,1/b,3*xs[1]*4*xs[0]]
