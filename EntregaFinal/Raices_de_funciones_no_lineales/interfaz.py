from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import bgcolor
from xml.etree.ElementTree import tostring
from numpy import size
from sympy import root, sympify


# Importar métodos numéricos desarrollados
from ridder import *

#----------------------------Ventana 1 ------------------------------------------------------------
root = Tk()
root.geometry('800x566')
root.resizable(0,0)  #No cambiar de tamaño
root.configure(bg='beige')

root.title("Métodos Numéricos")
root.iconbitmap(r"Recursos\logouca.ico")
imagen = PhotoImage(file = r"Recursos\fondo1.png")
lblImagen= Label(root,image=imagen).place(x=0, y=0)
imagenv2 = PhotoImage(file = r"Recursos\fondo2.png")
imagenv4 = PhotoImage(file = r"Recursos\fondo3.png")


#---------------------------------Funcion Ventana 2----------------------------------------
def v2():
    ventana2=Toplevel()
    ventana2.geometry('800x566')
    ventana2.resizable(0,0)  #No cambiar de tamaño
    ventana2.title("Métodos Numéricos")
    ventana2.configure(bg='beige')
    ventana2.iconbitmap(r"Recursos\logouca.ico")
    imagenv22 = Label(ventana2,image=imagenv2).place(x=0, y=0)
    button2 = Button(ventana2, text="Método de Halley", width=17, height=3,command = v4, font = ("Century Gothic", 9))
    button2.pack()
    button2.place(x=340, y = 250)
    button3 = Button(ventana2, text="Método de Ridder", width=17, height=3, command = v3, font = ("Century Gothic", 9) )
    button3.pack()
    button3.place(x=340, y = 350)
   


#----Boton ventana 1---------------------------------------------------------------
button1 = Button(root, text="Mostrar Métodos Empleados", width=30, height=3, command=v2)
button1.pack()
button1.place(x=290, y = 470)

#---------------------------------Funcion Ventana Ridder----------------------------------------
def v3():
    # Configuración de la ventana
    ridderWindow = Toplevel()
    ridderWindow.geometry('800x566')
    ridderWindow.resizable(0,0)
    ridderWindow.title("Método de Ridder")
    ridderWindow.iconbitmap(r"Recursos\logouca.ico")

    # Label
    imagenv44 = Label(ridderWindow, image=imagenv4)
    imagenv44.place(x = 0, y = 0)
    lblTitle = Label(ridderWindow, text = "Inserte los parámetros que se le indican", font = ("Century Gothic", 12), foreground="white", background="black")
    lblTitle.place(x = 225, y = 100)
    lblFunction = Label(ridderWindow, text = "F(x): ", font = ("Century Gothic", 12), foreground="white", background="black")
    lblFunction.place(x = 250, y = 150)
    lblA = Label(ridderWindow, text = "a: ", font = ("Century Gothic", 12), foreground="white", background="black")
    lblA.place(x = 250, y = 200)
    lblB = Label(ridderWindow, text = "b: ", font = ("Century Gothic", 12), foreground="white", background="black")
    lblB.place(x = 250, y = 250)
    lblTol = Label(ridderWindow, text = "TOL: ", font = ("Century Gothic", 12), foreground="white", background="black")
    lblTol.place(x = 250, y = 300)

    # Text box
    txtFunction = Entry(ridderWindow, font = ("Century Gothic", 12))
    txtFunction.place(x = 300, y = 150)
    txtA = Entry(ridderWindow, font = ("Century Gothic", 12))
    txtA.place(x = 300, y = 200)
    txtB = Entry(ridderWindow, font = ("Century Gothic", 12))
    txtB.place(x = 300, y = 250)
    txtTol = Entry(ridderWindow, font = ("Century Gothic", 12))
    txtTol.place(x = 300, y = 300)

    # Button
    def btnCalculate_clicked():
        # Get values and convert them to expressions
        strF = txtFunction.get()
        f_sym = sympify(strF)
        a = float(txtA.get())
        b = float(txtB.get())
        c = (a+b)*0.5
        tol = sympify(txtTol.get())

        # Get other values for generating pdf
        p, n, table = ridder(f_sym, a, b, tol)
        df = pd.DataFrame(table)
        g = g_function(f_sym, a, b, c)
        graph(f_sym, a, b, c, p, g, "Ridder")
        pdfGenerate(f_sym, a, b, c, tol, "prueba", df, n, p) 
        
    btnCalculate = Button(ridderWindow, text = "Calcular", width=17, height=3, font = ("Century Gothic", 9), command = btnCalculate_clicked, foreground="black", background="#ffde59")
    btnCalculate.place(x = 325, y = 350)

    #---------------------------------Funcion Ventana Halley----------------------------------------
def v4():
    # Configuración de la ventana
    halleyWindow = Toplevel()
    halleyWindow.geometry('800x566')
    halleyWindow.resizable(0,0)
    halleyWindow.title("Método de Halley")
    halleyWindow.iconbitmap(r"Recursos\logouca.ico")
    

    # Label
    imagenv44 = Label(halleyWindow,image=imagenv4).place(x=0, y=0)
    lblIndication = Label(halleyWindow, text = "Coloque los parametros que se le indican", font = ("Century Gothic", 14), foreground="white", background="black")
    lblIndication.pack()
    lblIndication.place(x = 220, y = 50)
    lblFunction2 = Label(halleyWindow, text = "F(x): ", font = ("Century Gothic", 12), foreground="white", background="black")
    lblFunction2.pack()
    lblFunction2.place(x = 250, y = 100)
    lblderivada1 = Label(halleyWindow, text = "F'(x): ", font = ("Century Gothic", 12), foreground="white", background="black")
    lblderivada1.place(x = 250, y = 150)
    lblderivada2 = Label(halleyWindow, text = "F''(x): ", font = ("Century Gothic", 12), foreground="white", background="black")
    lblderivada2.place(x = 250, y = 200)
    lblTol2 = Label(halleyWindow, text = "TOL: ", font = ("Century Gothic", 12), foreground="white", background="black")
    lblTol2.place(x = 250, y = 250)

    # Text box
    txtFunction2 = Entry(halleyWindow, font = ("Century Gothic", 12))
    txtFunction2.place(x = 300, y = 100)
    txtderivada1 = Entry(halleyWindow, font = ("Century Gothic", 12))
    txtderivada1.place(x = 300, y = 150)
    txtderivada2 = Entry(halleyWindow, font = ("Century Gothic", 12))
    txtderivada2.place(x = 300, y = 200)
    txtTol2 = Entry(halleyWindow, font = ("Century Gothic", 12))
    txtTol2.place(x = 300, y = 250)

    # Button
    btnCalculate2 = Button(halleyWindow, text = "Calcular", width=17, height=3, font = ("Century Gothic", 9))
    btnCalculate2.place(x = 300, y = 300)

root.mainloop()
