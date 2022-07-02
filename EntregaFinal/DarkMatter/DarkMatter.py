from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from turtle import bgcolor
from xml.etree.ElementTree import tostring
from matplotlib.pyplot import text
from numpy import size
from sympy import root, sympify





# Importar métodos numéricos desarrollados
from Metodos.ridder import *
from Metodos.halley import *


if __name__ == '__main__':

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
        lblFile_name = Label(ridderWindow, text = "Nombre: ", font = ("Century Gothic", 12), foreground="white", background="black")
        lblFile_name.place(x = 250, y = 350)

        # Text box
        txtFunction = Entry(ridderWindow, font = ("Century Gothic", 12))
        txtFunction.place(x = 350, y = 150)
        txtA = Entry(ridderWindow, font = ("Century Gothic", 12))
        txtA.place(x = 350, y = 200)
        txtB = Entry(ridderWindow, font = ("Century Gothic", 12))
        txtB.place(x = 350, y = 250)
        txtTol = Entry(ridderWindow, font = ("Century Gothic", 12))
        txtTol.place(x = 350, y = 300)
        txtFile_name = Entry(ridderWindow, font = ("Century Gothic", 12))
        txtFile_name.place(x = 350, y = 350)

        # Button
        def btnCalculate_clicked():
            # Get values and convert them to expressions
            try:
                # Get values and convert them to expressions
                strF = txtFunction.get()
                f_sym = sympify(strF)
                a = float(txtA.get())
                b = float(txtB.get())
                c = (a+b)*0.5
                tol = sympify(txtTol.get())
                file_name = txtFile_name.get()
                try:
                    result_labeL2.config(text="Reporte Generado y guardado en la carpeta métodos", foreground="white",background="black", font = ("Century Gothic", 12))
                    # Get other values for generating pdf
                    try:
                        # solve and get values
                        d, n, table = ridder(f_sym, a, b, tol)
                        df = pd.DataFrame(table)
                        k = asymptotic_error(table)
                        if n > 1:
                            g_sym = get_g_function(f_sym, a, b, c)
                            # Graphics
                            graphRidder(f_sym, a, b, c, file_name, d, g_sym)
                            graph_error(table, file_name, k)
                        # Create pdf
                        pdfGenerate (f_sym, a, b, c, tol, file_name, k, df, n, d)
                    except ValueError as error : 
                        messagebox.showerror(title='Error', message=str(error))
                except ValueError as error : 
                        messagebox.showerror(title='Error', message=str(error))        
            except ValueError as error : 
                    messagebox.showerror(title='Error', message=str(error))
            
        btnCalculate = Button(ridderWindow, text = "Calcular", width=17, height=3, font = ("Century Gothic", 9), command = btnCalculate_clicked, foreground="black", background="#ffde59")
        btnCalculate.place(x = 325, y = 400)
        #result report 
        result_labeL2 = Label(ridderWindow)
        result_labeL2.place(x = 110, y = 450)

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
        lblFunction2.place(x = 110, y = 150)
        lblTol2 = Label(halleyWindow, text = "TOL: ", font = ("Century Gothic", 12), foreground="white", background="black")
        lblTol2.place(x = 110, y = 200)
        lblIter2 = Label(halleyWindow, text = "Iter: ", font = ("Century Gothic", 12), foreground="white", background="black")
        lblIter2.place(x = 110, y = 250)
        lblInicial2 = Label(halleyWindow, text = "P0: ", font = ("Century Gothic", 12), foreground="white", background="black")
        lblInicial2.place(x = 110, y = 300)
        lblFilename = Label(halleyWindow, text = "File name: ", font = ("Century Gothic", 12), foreground="white", background="black")
        lblFilename.place(x = 110, y = 350)

        # Text box
        g_function = StringVar() #funcion donde se guardar el texto
        txtFunction2 = Entry(halleyWindow, textvariable=g_function, font = ("Century Gothic", 12))
        txtFunction2.place(x = 200, y = 150)
        txtFunction2.focus()

        tol2_function = StringVar()
        txtTol2 = Entry(halleyWindow, textvariable=tol2_function, font = ("Century Gothic", 12))
        txtTol2.place(x = 200, y = 200)

        iter2_function = StringVar()
        txtIter2 = Entry(halleyWindow, textvariable=iter2_function, font = ("Century Gothic", 12))
        txtIter2.place(x = 200, y = 250)

        inicial2_function = StringVar()
        txtInicial2 = Entry(halleyWindow, textvariable=inicial2_function , font = ("Century Gothic", 12))
        txtInicial2.place(x = 200, y = 300)

        filename_function = StringVar()
        txtFilename = Entry(halleyWindow, textvariable=filename_function , font = ("Century Gothic", 12))
        txtFilename.place(x = 200, y = 350)

        #-------------------------------------Button halley----------------------------------------------------->
        def clickbutton_clicked():
            try:
                p0 = float(inicial2_function.get())
                iter = float(iter2_function.get())
                tol = eval(tol2_function.get())
                f_str = g_function.get()
                file_name = filename_function.get()

                try:
                    result_label.config(text="Reporte Generado y guardado en la carpeta métodos", foreground="white",background="black", font = ("Century Gothic", 12))
                    try:
                        solve(p0, iter, f_str, tol,file_name)
                        
                    except ValueError as error:
                        messagebox.showerror(title="Error", message=str(error))
                except ValueError as error:
                        messagebox.showerror(title="Error", message=str(error))
            except ValueError as error:
                messagebox.showerror(title="Error", message=str(error))


        btnCalculate2 = Button(halleyWindow, text = "Calcular", width=15, height=2, font = ("Century Gothic", 10))
        btnCalculate2.place(x = 550, y = 300)
        btnCalculate2.configure(command=clickbutton_clicked)
        
        #-----------------------------------------Resultado label halley--------------------------------------->
        result_label = Label(halleyWindow)
        result_label.place(x = 110, y = 450)

    root.mainloop()
