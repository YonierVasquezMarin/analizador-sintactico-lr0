from Models.main import Main

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

main = Main(noTerminales, terminales, producciones)

print('imprimir lista producciones desde test')
for produccion in main.producciones:
    print(produccion)

# S -> .E
# E -> .E + T
# E -> .T
# T -> .T * F
# T -> .F
# F -> .id
# F -> .(E)