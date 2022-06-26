import math
import sympy as sp
from pylatex import Document, Section, Subsection, Command, Alignat
from pylatex.utils import NoEscape
import webbrowser

def ridder (f, a, b, TOL):
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


    return d

#-------------------------------------------------Function for writing math expressions
def write_math (doc, text):
    with doc.create(Alignat(numbering = False, escape = False)) as agn: 
        agn.append(text)

#-------------------------------------------------Function for generating a .pdf document
def pdfGenerate ():
    doc = Document()
    
    # Generating a title
    doc.preamble.append(Command("title", "Método de Ridder"))
    doc.append(NoEscape(r'\maketitle'))

    # First section
    with doc.create(Section("Datos")):
        doc.append("Función: ")
        #write_math(doc, f"f(x) = {sp.latex(f)}")
        doc.append ("Intérvalo a trabajar: ")
    
    # Generating .pdf and .tex documents 
    doc.generate_pdf("Método de Ridder", clean_tex=False)
    doc.generate_tex()
    webbrowser.open()