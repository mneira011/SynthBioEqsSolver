hours =1
import numpy as np
#constantes
a = 0

b=3

c=5

const = {'b': 3.0, 'a': 0.0, 'c': 5.0}
#valores iniciales
initVals = [3.0, 4.0]
#parametros en el diccionario
params = {'x': 'xs[0]', 'y': 'xs[1]'}
#parametros en el diccionario reversados
revparams = {'xs[0]': 'x', 'xs[1]': 'y'}
#ecuaciones diferenciales
def x(xs,const,t):
	return -3*xs[0]   +a  +1/b 
def y(xs,const,t):
	return -3*xs[1]   -1/b 
#arreglo de funciones
funcArray = [x, y]
#acciones
actions = [[1.0, 0.0], [0.0, 0.0], [-1.0, -2.0], [0.0, 2.0]]
#eventos
def darEventos(xs):
	return [3*xs[0],a,1/b,3*xs[1]]
