#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 15:23:13 2019

@author: fredy
"""

import math

# pasar de cordenadas cartesianas a esfericas, recibe cordenadas en x,y y z
def cartesianas_esfericas(x, y, z):
    try:
        r = round(math.sqrt(math.pow(x,2) + math.pow(y,2) + math.pow(z,2)),2)
        theta = round(math.degrees(math.acos(z/r)),2)
        fi = round(math.degrees(math.atan(y/z)),2)
        return (r, theta, fi)
    except ZeroDivisionError:        
        print("Division por cero!") 


def cartesianas_cilindricas(x, y, z):
    try:
        r = round(math.sqrt((x**2) + (y**2)),2)
        theta = round(math.degrees(math.atan(y/x)),2)
        z = z
        return (r, theta, z)
    except ZeroDivisionError:
        print("Division por cero!")

def cilindricas_esfericas(r, fi, z):
    try:
        r = round(math.sqrt(math.pow(r,2) + math.pow(z,2)),2)
        theta = round(math.degrees(math.atan(r/z)),2)
        fi = fi
        return (r , theta, fi)
    except ZeroDivisionError:
        print("Division por cero!")
        
def cilindricas_cartesianas(r, fi, z):
    
    x = round(r * math.cos(math.radians(fi)), 2)
    y = round(r * math.sin(math.radians(fi)), 2)
    z = z
    return (x , y, z)
    
    
def esfericas_cartesianas(r, theta, fi):
    
    x = round(r * math.sin(math.radians(theta)) * math.cos(math.radians(fi)), 2)
    y = round(r * math.sin(math.radians(theta)) * math.sin(math.radians(fi)), 2)
    z = round(r * math.cos(math.radians(theta)), 2)
    return (x, y, z)

def esfericas_cilindricas(r, theta, fi):
    
    r = round(r*math.sin(math.radians(theta)), 2)
    fi = fi
    z = round(r*math.cos(math.radians(theta)), 2)
    return (r, fi, z)
    