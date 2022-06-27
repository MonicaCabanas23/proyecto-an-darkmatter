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

#----------------------Grafica----------------------------------------->
#from pylab import *  da problemas con el boton de ventana 1

# importar el módulo pyplot

import matplotlib.pyplot as plt

from math import *
from numpy import *

#------------------------------------------documento-------------------------------------------------->
def write_math(doc, text):
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
        agn.append(text)

def write(doc, text):
    doc.append(text)

def write_pdf(f, f_sym, df, df_sym, d2f, d2f_sym, p0, iter, tol, file_name):
    geometry_options = {"tmargin": "1.5in", "lmargin": "1.5in"}
    doc = Document(geometry_options=geometry_options)
    
    with doc.create(Section("Halley")):
        with doc.create(Subsection("Datos")):
            write_math(doc, f"f(x) = {sp.latex(f_sym)}")
            write_math(doc, f"f'(x) = {sp.latex(df_sym)}")
            write_math(doc, f"f''(x) = {sp.latex(d2f_sym)}")
            write_math(doc, f"p0 = {p0}")
            write_math(doc, f"iter = {iter}")
            write_math(doc, f"\elipson  = {sp.latex(tol)}")
            
            with doc.create(Subsection("Validaciones")):
                write(doc, f"Evaluando en funcion f(x) los intervalos [{p0}, {iter}]: ")
                write_math(doc, f"\nf(p0) = {f(p0)}")
                write_math(doc,f"f(iter) = {f(iter)}")
                
                write(doc, "verificando derivada\n")
                write_math(doc, f"df(p0) = {df(p0)}")
                write_math(doc, f"df(iter) = {df(iter)}")
                
                if abs(df(p0)) < 1 and abs(df(iter)) < 1:
                    write(doc, "si cumple que tiene derivada ")
                else:
                    write(doc, "no cumple que tiene derivada")
                    
                    k = max(abs(p0), abs(iter))
                    write(doc, f"La cota para K en el intervalo [{p0}, {iter}] es: {k}")
                    max_dist = max(abs(p0 -p0), abs(iter - p0))
                    n_est = ceil(log(tol/max_dist)/log(k))
                    write(doc, f"Número de iteraciones estimadas: {abs(n_est)}")
                    write(doc, "Rapidez de convergencia:")
                    write_math(doc, f"O({round(k,2)}^n)")
                        
                    with doc.create(Subsection("Tabulaciones")):
                        write_math(doc, halley(f, df, d2f, p0, iter, tol))
                        
    create_doc(doc, file_name)
    open_doc(file_name)

    if abs(df(p0)) < 1 and abs(df(iter)) < 1:
          return False, 0
    
    k = max(abs(p0), abs(iter))

    max_dist = max(abs(p0 -p0), abs(iter - p0))
    n_est = ceil(log(tol/max_dist)/log(k))


#------------------------------------funcion al apretar el botón--------------------------------------->
def solve( p0, iter, f_str, tol, file_name):
        global x
        x = sp.Symbol("x")

        f_sym = sp.sympify(f_str)  #funcion simbolica
        f = sp.lambdify(x, f_sym)  #funcion f(x)
        df_sym = sp.diff(f_sym)   #derivada 1
        df = sp.lambdify(x, df_sym)   #funcion derivada 1
        d2f_sym = sp.diff(df_sym)  #derivada 2
        d2f = sp.lambdify(x, d2f_sym) #funcion derivada 2   
        write_pdf(f, f_sym, df, df_sym, d2f, d2f_sym, p0, iter, tol, file_name)

#---------------------------------------configurando webbrowser---------------------------------------->

def create_doc(doc, file_name):
    doc.generate_pdf(file_name, clean_tex=False)
    doc.generate_tex()

def open_doc(file_name):
    doc_path = f"{file_name}.pdf"
    webbrowser.open("file://" + os.path.realpath(doc_path)) 

