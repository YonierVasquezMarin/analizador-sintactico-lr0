from Models.control import Control
from Helpers.helper import Helper

noTerminales = ['S', 'E', 'T', 'F']
terminales = ['+', '*', '(', ')', 'k']
producciones = [
    ['S', 'E'],
    ['E', 'E+T'],
    ['E', 'T'],
    ['T', 'T*F'],
    ['T', 'F'],
    ['F', '(E)'],
    ['F', 'k']
]

control = Control(noTerminales, terminales, producciones)
produccionesI0 = control.estados[0].producciones
for produccion in produccionesI0:
    print(produccion)

# Helper para listas
# print("----------------------------------------------------------")
# noTerminales2 = "S, B, C"
# terminales2 = "a, d, b, c"
# produccion = "S -> aBCd\nB -> bb\nC -> cc"
# helper = Helper(noTerminales2, terminales2, produccion)
# print(helper.prepararListas(produccion))

################################################

# S -> .E
# E -> .E + T
# E -> .T
# T -> .T * F
# T -> .F
# F -> .id
# F -> .(E)