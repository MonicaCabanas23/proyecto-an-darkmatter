# Proyecto-AN

## Indicaciones Preliminares:

- El repositorio se usará para validar lo que se entregue en el Ecampus. Se espera un aporte equitativo de cada estudiante y dicho aporte se utilizará como multiplicador de la nota obtenida grupalmente.  
- Los documentos referentes a la segunda entrega deberán estar en la carpeta "SegundaEntrega", ubicada en la raíz de este repositorio.
- Los documentos referentes a la entrega final deberán estar en la carpeta "EntregaFinal", ubicada en la raíz de este repositorio.
- Crear un archivo "README.md" (sobreescribiendo este) en la raíz del repositorio que contenga:
	- Nombre del equipo
	- Módulo asignado
	- Métodos desarrollados
	- Nombre de cada estudiante y usuario de GitHub correspondiente
	- Carnet de cada estudiante


## Segunda Entrega

### Descripción

En esta entrega se deben implementar los métodos sustentados teóricamente en la entrega anterior. Para ello, se elaborará un Notebook de Jupyter en el cual se realicen distintos experimentos numéricos con los métodos asignados. Dichas implementaciones deberán ser aplicadas también a casos particulares, ilustrando con gráficos y tablas en caso de ser oportuno. En esta entrega, **los elementos ilustrativos deberán estar implementados con el lenguaje de programación**. 

Se permite el uso de paquetes, librerías o APIs necesarias para el desarrollo de dichos elementos como operaciones simbólicas y analíticas, generación de gráficas, tablas, archivos, etc. 
Sin embargo, no se permite la inclusión de métodos numéricos predefinidos en librerías externas que sean directamente los mismos que hayan sido asignados a cada grupo. 

El Notebook debe ir respectivamente documentado haciendo uso de celdas que contengan Markdown, y utilizar Latex para escribir expresiones matemáticas. El código debe ser claro y ordenado, además de estar comentado donde sea necesario. Todo lo implementado debe ser coherente con la base teórica de la primera entrega. 

Como ejemplo se pueden tomar los notebooks que se realizan en discusión.

### Productos a entregar:

- Notebook de Jupyter en formato .ipynb

### Recursos auxiliares: 

- [Numerical Tours in Python](http://www.numerical-tours.com/python/): Colección de notebooks de Jupyter programados en Python, elaborados por el matemático [Gabriel Peyré](http://www.gpeyre.com). Cada notebook presenta un tema de matemática aplicada y resultados numéricos correspondientes.
- [Graficación en Python con librería Matplotlib](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
- [Tabulación en Python con librería Pandas](https://pandas.pydata.org/pandas-docs/dev/getting_started/tutorials.html)
- [Arreglos numéricos en Python con NumPy](https://numpy.org/doc/stable/user/quickstart.html)
- [Operaciones simbólicas en Python con SymPy](https://docs.sympy.org/latest/tutorial/index.html)

El uso de todas estas librerías se ha ejemplificado a lo largo de las discusiones.

## Entrega Final 

### Descripción:

La entrega final del proyecto consiste en adaptar el código de la segunda entrega e implementarlos en una aplicación utilizable por un usuario. Dicha aplicación debe ser capaz de recibir entradas para que se utilicen en los métodos deseados, teniendo la capacidad de nevegar entre los dinstintos métodos o procesos que se soliciten.

La aplicación deberá contar con una interfaz gráfica amigable y al ejecutar dichos métodos se debe generar un reporte hecho en Latex, con formato PDF. Dicho reporte deberá contener los resultados del método, información que se considere relevante y elementos ilustrativos. 

Todas las etapas de cada proceso deberán ir debidamente validadas. 

Se entregará también un manual de usuario, donde se indique como se debe ejecutar el programa, se muestren instrucciones de llenado e indicaciones adicionales en caso de ser necesario. 

Además, se deberá presentar el funcionamiento de dicha aplicación en un video explicativo donde se muestre la participación de cada estudiante. Este video no debe exceder los 15 minutos de duración. 

La aplicación deberá ser desarrollada en el mismo lenguaje de programación que en la segunda entrega. 

### Productos a entregar:

- Ejecutable de la aplicación (para Windows)
- Manual de usuario
- Video explicativo

### Recursos auxiliares:

- [Interfaces gráficas en Python con Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Generación de documentos en Latex, desde Python con PyLatex](https://docs.python.org/3/library/tkinter.html)
- [Generación de ejecutables en Python con PyInstaller](https://docs.python.org/3/library/tkinter.html)

Como ejemplo se puede tomar la implementación de estas librerías con el ejecutable que se desarrolló en la [discusión #6](https://drive.google.com/file/d/1Gbf0WlboCOhX78b-zH19kdAABOsshz9d/view?usp=sharing).
