from lib2to3.pygram import Symbols
import math
from tkinter import messagebox
from pickle import NONE
from turtle import width
from matplotlib.font_manager import get_fontext_synonyms
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sympy as sp
from sympy import false, lambdify, sympify, Symbol, true 
from pylatex import Document, Section, Subsection, Command, Alignat, Tabular, Figure
from pylatex.utils import NoEscape
import webbrowser
import os

global pdf_created
pdf_created = false
#----------------------------------------------------------- Functions of Ridder Method
def ridder (f_sym, a, b, TOL):
    # Declaring variables to use
    x = Symbol('x')
    f = lambdify(x, f_sym)
        # Validating data
    try: 
        f(a)
    except ZeroDivisionError as error:
        messagebox.showerror(title='Error', message=str(error))
    try:
        f(b)
    except ZeroDivisionError as error:
        messagebox.showerror(title='Error', message=str(error))
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
    d = c
    oldRoot = c
    n = 1
    if f(a) * f(b) > 0:
        return d, n, table
    
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

def exponentialFactor (f, a, b, c):
    k = (f(c) + np.sign(f(b))*math.sqrt(f(c)**2 - f(a)*f(b)))/f(b)
    return k

def get_g_function(f_sym, a, b, c):
    x = Symbol('x')
    f = lambdify(x, f_sym)
    
    k = exponentialFactor(f, a, b, c)
    m = (f(b)*k**2 - f(a))/(b-a)
    p = f(c)*k
    # Using linear interpolation between a and b
    strg = str(m * (x - c) + p)  
    g_sym = sympify(strg)
    return g_sym

def asymptotic_error (table):
    length = len(table["ERROR"])
    sum = 0
    for i in range(0, length-1):
        l0 = table["ERROR"][i+1]/(table["ERROR"][i])**math.sqrt(2) # Asymptotic error constant
        sum += l0    
    avg = sum / (length - 1) # Calculating average for the asymptotic error constant
    return avg

#----------------------------------------------------------------------- Function for graphing
def graphRidder (f_sym, a, b, c, file_name, d, g_sym):
    x = Symbol('x')
    f = lambdify(x, f_sym)
    g = lambdify(x, g_sym)
    x = np.linspace(a, b, 100)
    d = c-(c-a)*f(c)/math.sqrt(f(c)**2-f(a)*f(b)) # first iteration

    f1 = plt.figure()
    plt.plot(x, [f(i) for i in x], label = 'f(x)', color = 'y')
    #f_df.plot(color = 'y')
    plt.plot([a, b, c, d],[f(a), f(b), f(c), f(d)], 'o', color = 'y')
    plt.plot(x, [g(i) for i in x], label = 'g(x)', color = 'b')
    #g_df.plot(color = 'b')
    plt.plot([a, b, c, d], [g(a), g(b), g(c), g(d)], 'o', color = 'b')
    plt.legend(loc = 'upper left')
    plt.xticks([a, b, c, d], ['a', 'b', 'c', 'd'])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.savefig(f"{file_name}_graph_Ridder.png", bbox_inches = "tight")

#---------------------------------------------------------------------- Graphing error
def graph_error(table, file_name, l = NONE):
    # Taking ridder as a quadratic order of convergence algorithm
    e = lambda n: l**(2**n-1)*(table["ERROR"][0])**2**n

    # Taking ridder as a sqrt(2) order of convergence algorithm
    def error (n):
        if n % 2 == 0:
            return l**((2**(n/2)-1)*(math.sqrt(2)+1))*(table["ERROR"][0])**(2**(n/4))
        else:
            return l**(2**((n+3)/2)-math.sqrt(2)-1)*(table["ERROR"][0])**(2**((n+3)/4))
    f2 = plt.figure()
    plt.plot(table["n"], [e(i) for i in table["n"]], label="Estimaci??n con orden de convergencia cuadr??tica", color="green")
    plt.plot(table["n"], [e(i) for i in table["n"]], 'o', color="green")
    plt.plot(table["n"], [error(i) for i in table["n"]], label="Estimaci??n con orden de convergencia sqrt(2)", color="red")
    plt.plot(table["n"], [error(i) for i in table["n"]], 'o', color="red")
    plt.plot(table["n"], table["ERROR"], label="Error real", color="blue")
    plt.plot(table["n"], table["ERROR"], 'o', color="blue")
    plt.legend(loc = "lower left")
    plt.grid()
    plt.title("Rapidez de convergencia")
    plt.xlabel("Iteraciones")
    plt.ylabel("Error absoluto")
    plt.yscale("log")
    plt.savefig(f"{file_name}_graph_error_Ridder.png", bbox_inches = "tight")

#-------------------------------------------------Functions for writing in the PDF doc
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
    image_filename = f"{file_name}_graph_Ridder.png"
    image_filename_1 = f"{file_name}_graph_error_Ridder.png"

    # Local variables and validations
    x = Symbol('x')
    f = lambdify(x, f_sym)
    c = 0.5 *(a + b)
    r = f(a) * f(b)
    s = math.sqrt(f(c)**2-f(a)*f(b))
    str_s = "sqrt(f(c)^2-f(a)*f(b))"
    s_sym = sympify(str_s)
    flag = true 
    
    # Generating a title
    doc.preamble.append(Command("title", "M??todo de Ridder"))
    doc.append(NoEscape(r'\maketitle'))

    # First section
    with doc.create(Section("Datos")):
        write_math(doc, f"f(x) = {sp.latex(f_sym)}")
        write_math(doc, f"a = {a}")
        write_math(doc, f"b = {b}")
        write_math(doc, f"TOL = {sp.latex(TOL)}")
    
    # Second section
    with doc.create(Section("Validaciones")):
        doc.append("Verificando que exista una ra??z dentro del int??rvalo inicial:\n")
        write_math(doc, f"f(a) * f(b) = {r}")
        doc.append("Verificando que no se ejecute una divisi??n entre cero:\n")
        write_math(doc, f"s = {sp.latex(s_sym)}")
        write_math(doc, f"s = {s}")
        if f(a) * f(b) > 0:
            doc.append("No existe una ra??z dentro del int??rvalo\n")
            flag = true
        if s == 0:
            doc.append("Se realiza una divisi??n entre cero dentro del m??todo, por lo tanto la funci??n no se puede evaluar:\n")
            flag = true

    # Third section
    if not df.empty and flag:
        with doc.create(Section("Ejecuci??n del m??todo")):
            # First subsection
            with doc.create(Subsection("Resultados num??ricos:")):
                doc.append("Al haber ejecutado el m??todo de Ridder se obtuvieron los siguientes datos:\n")
                doc.append("Ra??z aproximada:\n")
                write_math(doc, f"d = {d}")
                doc.append("N??mero de iteraciones: \n")
                write_math(doc, f"n = {n}")
            # Second subsection
            with doc.create(Subsection("Visualizaci??n de iteraciones y gr??ficas:")):
                # Table
                with doc.create(Subsection("Iteraciones")):
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
                            for c in range5:
                                row.append(df.loc[r][c])
                            table.add_row(row)
                        table.add_hline()
                # Graph
                with doc.create(Subsection("Gr??fica de f(x) y g(x) en la primera iteraci??n")):
                    with doc.create(Figure(position="h")) as graph:
                        graph.add_image(image_filename, width = "250px")
                with doc.create(Subsection("Gr??fica del error")):
                    with doc.create(Figure(position="h")) as graph:
                        graph.add_image(image_filename_1, width = "250px")

    # Fourth section
    with doc.create(Section("Conclusiones")):
        if n > 1:
            doc.append("El m??todo converge a 'd' en 'n' iteraciones\n")
            write_math(doc, f"d = {d}")
            write_math(doc, f"n = {n}")
            doc.append("La constante asint??tica te??rica del error del m??todo es: ")
            write_math(doc, f"k = {k}")
        else:
            doc.append("No existe ra??z dentro del int??rvalo especificado\n")

    
    # Generating .pdf and .tex documents 
    create_doc(doc, file_name)
    open_doc(file_name)
    pdf_created = true
