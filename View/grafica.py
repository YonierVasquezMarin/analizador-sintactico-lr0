import tkinter as tk


class Grafica:
    anchoVentana = 300
    altoVentana = 550
    noTerminales = ""
    terminales = ""
    producciones = ""

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Analizador LR0")
        self.vetana.geometry("{0}x{1}".format(
            self.anchoVentana, self.altoVentana
        ))
        self.ventana.resizable(width=False, height=False)
        self.ventana.mainloop()
