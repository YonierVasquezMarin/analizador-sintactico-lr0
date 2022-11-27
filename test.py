from Models.control import Control

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


################################################

# print('imprimir lista producciones desde test')
# for produccion in main.producciones:
#     print(produccion)

# S -> .E
# E -> .E + T
# E -> .T
# T -> .T * F
# T -> .F
# F -> .id
# F -> .(E)

# noTerminales = ['S', 'A']
# terminales = ['c', 'b']
# producciones = [
#     ['S', 'Ab'],
#     ['A', 'c'],
# ]
# control = Control(noTerminales, terminales, producciones)

# producciones = control.estados[0].producciones
# for produccion in producciones:
#     print(produccion)