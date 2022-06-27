#importando todas las funciones
import os as os
import matplotlib.pyplot as plt 
import sympy as sp
import numpy as np
import pandas as pd
from math import ceil, log
from math import *
from numpy import *
from math import exp, sqrt, sin, cos, pi
from sympy import *
from tabulate import tabulate
from pylatex import Document, Section, Subsection, Tabular, Math, TikZ, Plot, Figure, Alignat
from pylatex.utils import italic
import webbrowser

listahalley=[]

#----------------------------------Manejo de archivo-------------------------------------------------->
def remove_file(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)

def export_table(data_frame, file_name):
    remove_file(f"{file_name}.csv")
    remove_file(f"{file_name}.html")
    data_frame.to_csv(f"{file_name}.csv")
    data_frame.to_html(f"{file_name}.html")

#--------------------funcion de validar--------------------------------------------------------------->
def validate_f_funtion(df, p0, iter, tol):
    
    if abs(df(p0)) < 1 and abs(df(iter)) < 1:
          return False, 0
    
    k = max(abs(p0), abs(iter))

    max_dist = max(abs(p0 -p0), abs(iter - p0))
    n_est = ceil(log(tol/max_dist)/log(k))
    
    return True, n_est

#--------------------------------Algoritmo de halley------------------------------------------------->

def halley(f, df, d2f, p0, iter, tol):   #definiendo la función halley
    p=p0                                 #sobredefiniendo p0
    lista=[]
    pp="-"                              
    error="-"
    for i in [*range(0, int(float(iter)))]:   #ciclo for para tomar encuenta el intervalo [0,pi]
        lista.append([i,p,f(p),df(p),error]) 
        listahalley.append(p)
        pp=p
        p=p-2*f(p)*df(p)/2*df(p)**2-f(p)*d2f(p) #formula de halley
        errorA=abs(p-pp)                        #encontrar el error de halley
        if p!=0:                                #iteraciones hasta encontrar 0
            errorB=abs(p-pp)/p
        errorC=abs(f(p))
        error=errorA
        if error<tol:                          #parar hasta que error sea menor que la tolerancia
            break                                 
    print(tabulate(lista,headers=["n","pn","f(pn)","f'(pn)","error"],tablefmt='fancy_grid')) #imprimiendo resultados en tabulaciones
    return p