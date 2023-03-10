#importando todas las funciones
from fileinput import filename
import os as os
from IPython.display import display
import matplotlib.pyplot as plt 
import sympy as sp
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import ceil, log
from math import *
from numpy import *
from math import exp, sqrt, sin, cos, pi
from sympy import *
from tabulate import tabulate
from pylatex import Document, Section, Subsection, Subsubsection, Tabular, Figure, Alignat,Command
from pylatex.utils import italic,  NoEscape
import webbrowser
import os



listahalley=[]
lista=[]




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

#algoritmo de halley
def halley(f, df, d2f, p0, iter, tol):                         #definiendo la función halley
    p=p0                                 #sobredefiniendo p0
    lista=[]                             #definiendo lista simple
    pp="-"                              
    error="-"
    table = {"n":[],
        "pn":[],
        "f(pn)":[],
        "f'(pn)":[],
        "error":[]}
    n = 0

    for i in [*range(0, int(float(iter)))]:   #ciclo for para tomar encuenta el intervalo [0,pi]
        lista.append([i,p,f(p),df(p),error]) 
        listahalley.append(p)
        table["n"].append(i)
        table["pn"].append(p)
        table["f(pn)"].append(f(p))
        table["f'(pn)"].append(df(p))
        table["error"].append(error)
        n +=1

        pp=p
        p=p-2*f(p)*df(p)/2*df(p)**2-f(p)*d2f(p) #formula de halley 
        
        errorA=abs(p-pp)                        #encontrar el error de halley
        if p!=0:
            errorB=abs(p-pp)/p
        errorC=abs(f(p))
        error=errorA
        if error<tol:                          #parar hasta que error sea menor que la tolerancia
            break  
    return p, table, n
#--------------------------------------------Grafica------------------------------------------------------>
def graph(file_name, f):
    plt.clf()
    x = arange(0.1, 20, 0.1)

    f3 = plt.figure
    plt.plot(x, [f(i) for i in x])
    # Establecer el color de los ejes.
    plt.axhline(0, color="black")
    plt.axvline(0, color="black")
    # Limitar los valores de los ejes.
    
    # Guardar gráfico como imágen PNG.
    plt.grid()
    # Mostrarlo.
    plt.savefig(f"{file_name}_graph.png", bbox_inches="tight" )


#------------------------------------------documento-------------------------------------------------->
def write_math(doc, text):
    with doc.create(Alignat(numbering=False, escape=False)) as agn:
        agn.append(text)

def write(doc, text):
    doc.append(text)

 

def write_pdf(f, f_sym, df, df_sym, d2f, d2f_sym, p0, iter, tol, file_name):
    geometry_options = {"tmargin": "1.5 in", "lmargin": "1.5in"}
    doc = Document(geometry_options=geometry_options)
    image_filename = f"{file_name}_graph.png"
    p, table, n = halley(f, df, d2f, p0, iter, tol)

    doc.preamble.append(Command("title", "Método de Halley"))
    doc.append(NoEscape(r'\maketitle'))
    
    with doc.create(Section("Desarrollo del problema")):
        with doc.create(Subsection("Datos")):
            write_math(doc, f"f(x) = {sp.latex(f_sym)}")
            write_math(doc, f"f'(x) = {sp.latex(df_sym)}")
            write_math(doc, f"f''(x) = {sp.latex(d2f_sym)}")
            write_math(doc, f"p0 = {p0}")
            write_math(doc, f"iter = {iter}")
            write_math(doc, f"\epsilon  = {sp.latex(tol)}")
            
            
        with doc.create(Subsection("Validaciones")):
            with doc.create(Subsubsection("Evaluando la función en los intervalos")):
                write(doc, f"Evaluando en funcion f(x) los intervalos [{p0}, {iter}]: \n")
                write(doc, "\nEvaluando el punto inicial en la función\n")
                write_math(doc, f"f(p0) = {f(p0)}")
                write(doc, "\nEvaluando la iteración o punto final en función\n")
                write_math(doc,f"f(iter) = {f(iter)}")

            with doc.create(Subsubsection("Evaluando si existe la derivada")): 
                write(doc, "verificando derivada\n")
                write(doc, "\nEvaluando la punto inicial en primera derivada\n")
                write_math(doc, f"df(p0) = {df(p0)}")
                write(doc, "\nEvaluando la iteración en primera derivada\n")
                write_math(doc, f"df(iter) = {df(iter)}")
                
                if abs(df(p0)) < 1 and abs(df(iter)) < 1:
                    write(doc, "Si tiene derivada, procedemos al desarrollo del problema...")
                else:
                    write(doc, "No tiene derivada")


            with doc.create(Subsubsection("verificando la cota k en el intérvalo")):
                
                k = max(abs(p0), abs(iter))
                write(doc, f"\nLa cota para K en el intérvalo [{p0}, {iter}] es: {k}\n")
                max_dist = max(abs(p0 -p0), abs(iter - p0))
                n_est = ceil(log(tol/max_dist)/log(k))

            with doc.create(Subsubsection("Evaluando iteraciones estimadas")):
                write(doc, f"\nNúmero de iteraciones estimadas: {abs(n_est)}\n")
            
            with doc.create(Subsubsection("Evaluando Rapides de Convergencia")):
                write(doc, "\nRapidez de convergencia:")
                write_math(doc, f"O({round(k,2)}^n)")

        with doc.create(Subsection("Iteraciones")):
            with doc.create(Subsubsection("Resultado de raíz aproximada del problema")):
                write(doc, "Valor de raíz aproximada:")
                write_math(doc, sp.latex(p))
                with doc.create(Subsubsection("Resultado de iteraciones de la función")):
                
                    df = pd.DataFrame(table)
                    with doc.create(Tabular("c|c|c|c|c")) as table:
                        range1 = {0, 1, 2, 3, 4}
                        table.add_hline()
                        table.add_row(df.columns)
                        for r in range(n):
                            row = []
                            for c in range1:
                                row.append(df.loc[r][c])
                            table.add_row(row)
                        table.add_hline()

        with doc.create(Subsection("Visualización de grafica")):
                    write_math(doc, f"\nGrafica para la función")
                    write_math(doc, f"f(x) = {sp.latex(f_sym)}")
                    with doc.create(Figure(position="h")) as graph:
                        graph.add_image(image_filename, width = "250px")                 
    doc.generate_pdf(file_name, clean_tex=False)
   

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
        graph(file_name, f)
        write_pdf(f, f_sym, df, df_sym, d2f, d2f_sym, p0, iter, tol, file_name)
        webbrowser.open(f"{file_name}.pdf")



