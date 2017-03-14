import numpy as np
#constantes

a = 0

b=3

c=5

#condiciones inciales

x0 = 3

t0= 2

#ecuaciones diferenciales
def x(x,t,xgh):
	return 3*x*4*t  -2  +a 
def dx(x,t,xgh):
	return 3*xgh*4*t  -2" 
