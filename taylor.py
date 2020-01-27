# -*- coding: utf-8 -*-

"""
Created on Sat Dec  8 13:43:13 2018

@author: Fredy

"""
from sympy import diff, Symbol, sin, cos
import math

"""
definicion de variables en la funcion

z=Symbol('z') para agregar la variable z

"""
x = Symbol('x')
y = Symbol('y')

variables = [x, y]


"""
1-> ((y**2)*x+(y**3))

2-> 1/((x**2)+(y**2)+1)

3-> exp(x)*cos(x+y)
"""

#funcs = vars(math)
#libres = dict(x=0, y=0)
#s = "1/((x**2)+(y**2)+1)"
#print(eval(s, funcs, libres))

def taylor(funcion,X,Y):# (funcion, numero de variables)
    n = 2
    t = x-X
    t1 = y-Y
    taylor = []
    
	"""
	evalua la funcion original
	"""
    funcs=vars(math)
    libres=dict(x=X, y=Y)
    origin=eval(funcion, funcs, libres)
    taylor.append(origin)
    
	"""
	realiza el calculo de la primera derivada respecto a 'x' y 'y'
	"""
    for k in variables:
        derivadas = diff(funcion,k)
        #print(derivadas)
        evalfunc = derivadas.evalf(subs={x:X, y:Y}, n=3)
        if(k==x):
            res = evalfunc*t
            if(res!=0):
                taylor.append(res)
        if(k==y):
            res = evalfunc*t1
            if(res!=0):
                taylor.append(res)
           
        #print("derivada respecto de ", k," ",evalfunc)
    """
	Realiza el calculo y evalua las derivadas cruzadas y derivadas dobles respecto de cada variable 'x' y 'y'
	"""

    for i in range(n):
        for j in range(n):
            derivadas = (1/2) * diff(diff(funcion,variables[j]), variables[i])
            #print(derivadas)
            evalfunc = derivadas.evalf(subs={x:X,y:Y}, n=3),# evalua la func, en los puntos datos, n=3 corresponde al numero de digitos despues del 0.

            if(variables[i] == variables[j] == x): # segun la derivada, se multiplica por el cuadrado, t y t1 estan definidas al inicio
                res = evalfunc*t**2
                if(res!=0):
                    taylor.append(res)
            if(variables[i] == variables[j] == y):
                res = evalfunc*t1**2 
                if(res!=0):
                    taylor.append(res)
			"""
			Se multiplican las derivadas cruzadas
			"""
            if((variables[i] == x and variables[j] == y) or (variables[i] == y and variables[j] == x)):
                res = evalfunc*t*t1
                if(res!=0):
                    taylor.append(res) # cada derivada evaluada se agrega al polinimio              
    print("Polinomio: ", list(taylor))



if __name__=='__main__':
    
    print("Ingresa una funcion: ")
    funcion = input("-->: ")
    X = input("x: ")
    Y = input("y: ")
    
    try:
        X=int(X)
        Y=int(Y)
        taylor(funcion,X,Y)
        
    except:
        print("Los puntos x,y deben ser un numero...")
