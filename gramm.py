# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:58:04 2018

@author: Fredy
"""

import numpy

"""
la func recibe dos vectores, realiza el producto punto de dos vectores y la division, regresa un escalar
"""
def gs_cofficient(v1, v2):

    return (numpy.dot(v2, v1)/numpy.dot(v1, v1))

"""
funcion que recive dos vectores y calcula la proyeccion del vector v1 sobre v2, regresa un vector
"""
def proj(v1, v2):
    
    return (numpy.multiply(gs_cofficient(v1, v2) , v1))

"""
recibe un conjunto de vectores en Rn y realiza el proceso de ortogonolizacion de gram

"""
def gs(vectores):
   
    Y = []
    
    for vector in vectores:
        temp_vec = vector
        for inY in Y :
            proj_vec = proj(inY, vector)
            temp_vec =list(temp_vec - proj_vec)# toma el vector anterior y realiza la resta de la proyeccion de vectores
        Y.append(temp_vec)
    return (Y)

# vectores de ejemplo
# [0,1,2], [1, 0,0],[0,1,1]
# [1, 1, 1], [1, 0, 2], [1, 0, 0]
# [2, 1,1], [1, 0,10],[2,-3,11]
# [1, 1, 1], [1, 0, 2], [1, 0, 0]

if __name__ == '__main__':
    
    test = numpy.array([[1, 1, 1], [1, 0, 2], [1, 0, 0]])
    print (numpy.array(gs(test)))






