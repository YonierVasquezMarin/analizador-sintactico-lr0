import tkinter as tk
from tkinter import ttk


class Grafica:
    anchoVentana = 300
    altoVentana = 550
    noTerminales = ""
    terminales = ""
    producciones = ""

    def __init__(self):
        # self.callback = callback
        self.ventana = tk.Tk()
        self.ventana.title("Analizador LR0")
        self.ventana.geometry("{0}x{1}".format(
            self.anchoVentana, self.altoVentana
        ))
        self.ventana.resizable(width=False, height=False)
        self.crearEntradas()
        self.ventana.mainloop()

    def crearEntradas(self):
        l = tk.Label(self.ventana, text="Ingrese los no terminales: ")
        l.pack()
        self.entry = tk.Entry(self.ventana)
        self.entry.pack()

        l2 = tk.Label(self.ventana, text="Ingrese los terminales: ")
        l2.pack()
        self.entry2 = tk.Entry(self.ventana)
        self.entry2.pack()

        l3 = tk.Label(self.ventana, text="Ingrese las producciones: ")
        l3.pack()
        self.entry3 = tk.Text(self.ventana)
        self.entry3.pack(padx=10)

        button = tk.Button(self.ventana, text="Generar Análisis",
                           bg="light blue", borderwidth=5, command=lambda: self.ejecutar())
        button.pack()

    def ejecutar(self) -> None:
        '''
        Reset de las variables
        '''
        self.noTerminales = ''
        self.terminales = ''
        self.producciones = ''
        self.capturarEntradas()

    def capturarEntradas(self):
        self.noTerminales = self.entry.get()
        self.terminales = self.entry2.get()
        self.producciones = self.entry3.get("1.0", 'end-1c')
        # listaRetorno = self.callback(
        #     self.noTerminales, self.terminales, self.producciones)
        # textoNoTerminales = ""
        # textoTerminales = ""
        # textoConjuntoPrediccion = ""
        # for i in listaRetorno[0]:
        #     textoNoTerminales += str(i) + "\n"
        # for i in listaRetorno[1]:
        #     textoTerminales += str(i) + "\n"
        # for i in listaRetorno[2]:
        #     textoConjuntoPrediccion += str(i) + "\n"

        cadena = [
            'I-0\nS -> .A\nA -> .(A)\nA -> .a\nTransicion A a I1\nTransicion ( a I2\nTransicion a I4', 'I-1\nS -> A. [R0]']
        print(tuple(cadena))
        self.generarVentanaResultado(cadena)

    def generarVentanaResultado(self, listaEstados=[]):
        '''Genera la ventana con el resultado del análisis LL1'''
        # Valores por defecto
        self.ventanaResultado = tk.Tk()
        self.ventanaResultado.title("Resultado análisis LR0")
        self.ventana.geometry("{0}x{1}".format(
            self.anchoVentana, self.altoVentana
        ))
        self.__generarTabla(listaEstados)
        self.ventanaResultado.mainloop()

    def __generarTabla(self, listaEstados: str):
        treeView = ttk.Treeview(self.ventanaResultado,
                                columns=tuple(listaEstados))

        treeView.grid(column=0, row=0)
        count = 1
        for i in listaEstados:
            treeView.column("#{}".format(str(count)))
            treeView.heading("#{}".format(str(count)), text=i[0:3])
            count = count + 1
        # En caso de no tener columnas bien distribuidas
        treeView.column("#0", width=0)
        for i in range(1, len(listaEstados)):
            treeView.insert("", i, values=tuple(listaEstados))
