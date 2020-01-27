# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 17:26:19 2018

@author: Fredy
"""

import funciones
    
def menu():
    

    done = 1
    
    while (done == 1):
        print('################  Cambio de coordenadas  ################')
        print('Selecciona una opcion:')
        print('\t1 - Cartesianas a Esfericas')
        print('\t2 - Cartesianas a Cilindricas')
        print('\t3 - Esfericas a Cilindricas')
        print('\t4 - Esfericas a Cartesianas')
        print('\t5 - Cilindricas a Cartesianas')
        print('\t6 - Cilindricas a Esfericas')
        print('\t0 - Salir')
        opcionMenu = input('Opcion >> ')
        try:
            opcionMenu=int(opcionMenu)
            
            if (opcionMenu == 1):#Cartesianas a Esfericas
                x = input('x = ')
                y = input('y = ')
                z = input('z = ')
                try:
                    x=int(x)
                    y=int(y)
                    z=int(z)
                    cartesianas=funciones.cartesianas_esfericas(x, y, z)
                    print(cartesianas)
                    print('\n\n')
                except ValueError:
                    print("Debe ser un entero!")

            if (opcionMenu == 2):#Cartesianas a Cilindricas
                x = input('x = ')
                y = input('y = ')
                z = input('z = ')
                try:
                    x=int(x)
                    y=int(y)
                    z=int(z)                    
                    cartesianas=funciones.cartesianas_cilindricas(x, y, z)
                    print(cartesianas)
                    print('\n\n')
                except ValueError:
                    print("Debe ser un entero!")
    
            if (opcionMenu == 3):#Esfericas a Cilindricas
                r = input('r = ')
                theta = input('theta = ')
                fi = input('fi = ')
                try:
                    r=int(r)
                    theta=int(theta)
                    fi=int(fi)
                    esfericas=funciones.esfericas_cilindricas(r, theta, fi)
                    print(esfericas)
                    print('\n\n')
                except ValueError:
                    print("Debe ser un entero!")
    
            if (opcionMenu == 4):#Esfericas a Cartesianas
                r = int(input('r = '))
                theta = int(input('theta = '))
                fi = int(input('fi = '))
                try:
                    r=int(r)
                    theta=int(theta)
                    fi=int(fi)                    
                    esfericas=funciones.esfericas_cartesianas(r, theta, fi)
                    print(esfericas)
                    print('\n\n')
                except ValueError:
                    print("Debe ser un entero!")
    
            if (opcionMenu == 5):#Cilindricas a Cartesianas
                r = input('r = ')
                fi = input('theta = ')
                z = input('fi = ')
                try:
                    r=int(r)
                    fi=int(fi)
                    z=int(z)
                    cilindricas=funciones.cilindricas_cartesianas(r, fi, z)
                    print(cilindricas)
                    print('\n\n')
                except ValueError:
                    print("Debe ser un entero!")
                    
            if (opcionMenu == 6):#Cilindricas a Esfericas
                r = input('r = ')
                fi = input('theta = ')
                z = input('fi = ')
                try:
                    r=int(r)
                    fi=int(fi)
                    z=int(z)
                    cilindricas=esfericas.cilindricas_esfericas(r, fi, z)
                    print(cilindricas)
                    print('\n\n')
                except ValueError:
                    print("Debe ser un entero!")
            
            if (opcionMenu == 0):
                done = 0
        
        except ValueError:
            print("Debe ser un numero!")            

if __name__=='__main__':
    menu()
    
    
    
    