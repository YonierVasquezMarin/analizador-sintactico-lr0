from Models.control import Control
from Helpers.helper import Helper


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
# terminales = ['(', ')', 'a']
# noTerminales = ['S', 'A']
# producciones = [
# 	['S', 'A'],
# 	['A', '(A)'],
# 	['A', 'a']
# ]
# control = Control(noTerminales, terminales, producciones)

# for estado in control.estados:
# 	print(estado)

# Funciona
# terminales = ['n', '+']
# noTerminales = ['E']
# producciones = [
# 	['E', 'E+n'],
# 	['E', 'n']
# ]
# control = Control(noTerminales, terminales, producciones)

# for estado in control.estados:
# 	print(estado)

# Funciona
# terminales = ['(', ')', 'a']
# noTerminales = ['A']
# producciones = [
# 	['A', '(A)'],
# 	['A', 'a']
# ]
# control = Control(noTerminales, terminales, producciones)

# for estado in control.estados:
# 	print(estado)