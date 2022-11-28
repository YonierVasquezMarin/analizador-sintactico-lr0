from Models.control import Control
from Helpers.helper import Helper


# produccionesI0 = control.estados[0].producciones
# for produccion in produccionesI0:
#     print(produccion)

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

# Funciona
# terminales = ['b', 'c']
# noTerminales = ['S', 'A', 'M']
# producciones = [
# 	['S', 'Ab'],
# 	['A', 'M'],
# 	['M', 'c']
# ]
# control = Control(noTerminales, terminales, producciones)

# Funciona
terminales = ['(', ')', 'a']
noTerminales = ['S', 'A']
producciones = [
	['S', 'A'],
	['A', '(A)'],
	['A', 'a']
]
control = Control(noTerminales, terminales, producciones)

for estado in control.estados:
	print(estado)