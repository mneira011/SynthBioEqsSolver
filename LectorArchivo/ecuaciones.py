import numpy as np
#constantes
a = 0

b=3

c=5

const = {'a': 0.0, 'b': 3.0, 'c': 5.0}
#valores iniciales
initVals = [3.0, 4.0]
#parametros en el diccionario
params = {'y': 'xs[1]', 'x': 'xs[0]'}
#parametros en el diccionario reversados
revparams = {'xs[1]': 'y', 'xs[0]': 'x'}
#ecuaciones diferenciales
def x(xs,const,t):
	return -3*xs[0]*4*xs[1]  -2  +a 
def y(xs,const,t):
	return -3*xs[1]*4*xs[0]  -2 
funcArray = [y, x]
def darEventos(xs):
	return [-3*xs[0]*4*xs[1] ,-2 ,+a,-3*xs[1]*4*xs[0] ,-2]
funcArray = [y, x]
def darEventos(xs):
	return [-3*xs[0]*4*xs[1] ,-2 ,+a,-3*xs[1]*4*xs[0] ,-2]
