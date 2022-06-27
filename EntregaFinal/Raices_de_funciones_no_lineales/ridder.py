import math
from pickle import NONE
from turtle import width
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
from sympy import lambdify, sin, cos, sympify, tan, asin, acos, Symbol 
from pylatex import Document, Section, Subsection, Command, Alignat, Tabular, Figure
from pylatex.utils import NoEscape
import webbrowser
import os

#----------------------------------------------------------- Method algorithms
def ridder (f_sym, a, b, TOL):
    # Declaring variables to use
    x = Symbol('x')
    f = lambdify(x, f_sym)
    table = {"n":[],
        "a":[],
        "b":[],
        "f(a)":[],
        "f(b)":[],
        "c":[],
        "f(c)":[],
        "f(a)-f(b)":[],
        "d":[],
        "f(d)":[],
        "ERROR":[]}
    c = 0.5 * (a + b)
    oldRoot = c
    n = 1
    
    while True:
        # Executing iteration of the method
        c = 0.5 * (a + b)
        s = math.sqrt(f(c)**2-f(a)*f(b))
        if s == 0:
            d = c
            break
            
        if f(a) - f(b) > 0:
            d = c+(c-a)*f(c)/math.sqrt(f(c)**2-f(a)*f(b))
        else:
            d = c-(c-a)*f(c)/math.sqrt(f(c)**2-f(a)*f(b))

        # Saving data in a table
        table["n"].append(n)
        table["a"].append(a)
        table["b"].append(b)
        table["f(a)"].append(f(a))
        table["f(b)"].append(f(b))
        table["c"].append(c)
        table["f(c)"].append(f(c))
        table["f(a)-f(b)"].append(f(a)-f(b))
        table["d"].append(d)
        table["f(d)"].append(f(d))
        table["ERROR"].append(abs(oldRoot-d))
       
        # Finding the new interval
        if f(c) * f(d) <= 0:
            if c < d: 
                a = c
                b = d
            else:
                a = d
                b = c
        else:
            if f(b) * f(d) < 0:
                a = d
            else: 
                b = d
        
        # Evaluating error
        if abs(oldRoot - d) <= TOL:
            break
        oldRoot = d
        n+=1

    return d, n, table

def asymptotic_error (table):
    length = len(table["ERROR"])
    sum = 0
    for i in range(0, length-1):
        l0 = table["ERROR"][i+1]/(table["ERROR"][i])**math.sqrt(2) # Asymptotic error constant
        sum += l0    
    avg = sum / (length - 1) # Calculating average for the asymptotic error constant
    return avg

#-------------------------------------------------Function for writing math expressions
def write_math (doc, text):
    with doc.create(Alignat(numbering = False, escape = False)) as agn: 
        agn.append(text)

def create_doc(doc, file_name):
    doc.generate_pdf(file_name, clean_tex=False)
    doc.generate_tex()

def open_doc(file_name):
    doc_path = f"{file_name}.pdf"
    webbrowser.open("file://" + os.path.realpath(doc_path)) 
#-------------------------------------------------Function for generating a .pdf document
def pdfGenerate (f_sym, a, b, c, TOL, file_name, k = NONE, df = pd.DataFrame({}), n = NONE, d = NONE):
    geometry_options = {"tmargin": "1.5 in", "lmargin": "1.5in"}
    doc = Document(geometry_options=geometry_options)
    k_error = k
    # Validations
    x = Symbol('x')
    f = lambdify(x, f_sym)
    c = 0.5 *(a + b)
    r = f(a) * f(b)
    s = math.sqrt(f(c)**2-f(a)*f(b))
    str_s = "sqrt(f(c)^2-f(a)*f(b))"
    s_sym = sympify(str_s)
    
    # Generating a title
    doc.preamble.append(Command("title", "Método de Ridder"))
    doc.append(NoEscape(r'\maketitle'))

    # First section
    with doc.create(Section("Datos")):
        write_math(doc, f"f(x) = {sp.latex(f_sym)}")
        write_math(doc, f"a = {a}")
        write_math(doc, f"b = {b}")
        write_math(doc, f"TOL = {sp.latex(TOL)}")
    
    # Second section
    with doc.create(Section("Validaciones")):
        doc.append("Verificando que exista una raíz dentro del intérvalo inicial:\n")
        write_math(doc, f"f(a) * f(b) = {r}")
        doc.append("Verificando que no se ejecute una división entre cero:\n")
        write_math(doc, f"s = {sp.latex(s_sym)}")
        write_math(doc, f"s = {s}")
        if f(a) * f(b) > 0:
            doc.append("No existe una raíz dentro del intérvalo\n")
        if s == 0:
            doc.append("Se realiza una división entre cero dentro del método, por lo tanto la función no se puede evaluar:\n")
    
    # Third section
    if not df.empty:
        with doc.create(Section("Ejecución del método")):
            # First subsection
            with doc.create(Subsection("Resultados numéricos:")):
                doc.append("Al haber ejecutado el método de Ridder se obtuvieron los siguientes datos:\n")
                doc.append("Raíz aproximada:\n")
                write_math(doc, f"d = {d}")
                doc.append("Número de iteraciones: \n")
                write_math(doc, f"n = {n}")
            # Second subsection
            with doc.create(Subsection("Visualización de iteraciones:")):
                # Table
                with doc.create(Tabular("c|c")) as table:
                    range1 = {1, 2}
                    range2 = {3, 4}
                    range3 = {5, 6}
                    range4 = {7, 8}
                    range5 = {9, 10}
                    table.add_hline()
                    table.add_row(df.columns[1], df.columns[2])
                    for r in range(n):
                        row = []
                        for c in range1:
                            row.append(df.loc[r][c])
                        table.add_row(row)
                    table.add_hline()
                    table.add_row(df.columns[3], df.columns[4])
                    table.add_hline()
                    for r in range(n):
                        row = []
                        for c in range2:
                            row.append(df.loc[r][c])
                        table.add_row(row)
                    table.add_hline()
                    table.add_row(df.columns[5], df.columns[6])
                    table.add_hline()
                    for r in range(n):
                        row = []
                        for c in range3:
                            row.append(df.loc[r][c])
                        table.add_row(row)
                    table.add_hline()
                    table.add_row(df.columns[7], df.columns[8])
                    table.add_hline()
                    for r in range(n):
                        row = []
                        for c in range4:
                            row.append(df.loc[r][c])
                        table.add_row(row)
                    table.add_hline()
                    table.add_row(df.columns[9], df.columns[10])
                    table.add_hline()
                    for r in range(n):
                        row = []
                        for c in range4:
                            row.append(df.loc[r][c])
                        table.add_row(row)
                    table.add_hline()

    # Fourth section
    with doc.create(Section("Conclusiones")):
       doc.append("El método converge a 'd' en 'n' iteraciones\n")
       write_math(doc, f"d = {d}")
       write_math(doc, f"n = {n}")
       doc.append("La constante asintótica teórica del error del método es: ")
       write_math(doc, f"k = {k}")
    
    # Generating .pdf and .tex documents 
    create_doc(doc, file_name)
    open_doc(file_name)
