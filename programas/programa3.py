import sys
import io
import nltk
from nltk.tree import Tree



Masc = {'descubre': 'es descubierto por','aplasta': 'es aplastado por','come': 'es comido por','salta': 'es saltado por','trepa': 'es trepado por'}

Fem = {'aplasta': 'es aplastada por','come': 'es comida por','descubre': 'es descubierta por','salta': 'es saltada por','trepa': 'es trepada por'}

"""
la = {es comida, es saltada, es trepada, es descubierta, es aplastada}
el = {es comido, es saltado, es trepado, es descubierto, es aplastado}
un = {es comido, es saltado, es trepado, es descubierto, es aplastado}
una = {es comida, es saltada, es trepada, es descubierta, es aplastada}
esa = {es comida, es saltada, es trepada, es descubierta, es aplastada}
ese = {es comido, es saltado, es trepado, es descubierto, es aplastado}
tu -> depende del nominal

la = una = esa
el = un =ese

Nominales: 
    masculinos = {kiwi, mango, perro, gato, elefante, hueso, pescado }
    femeninos = {manzana, banana, naranja, pera, frutilla, perra, gata}

"""

def parse(s):
    
    grammar = """
    S -> A V C | Z V C
    C -> Z | A 
    Z -> P J | TY
    A -> O Y | B
    TY -> 'Marta' | 'Julia'
    B -> 'Juan' | 'Pedro'
    P -> 'una' | 'esa' | 'la' | 'tu'
    J -> 'banana' | 'naranja' | 'manzana' | 'gata' | 'pera' | 'frutilla' | 'perra' | 'elefante'
    Y -> 'mango' | 'gato' | 'elefante' | 'kiwi' | 'hueso' | 'pescado' | 'perro'
    O -> 'el' | 'un' | 'ese' | 'tu'
    V -> 'come' | 'salta' | 'trepa' | 'descubre' | 'aplasta'
    """
    
    grammar = nltk.CFG.fromstring(grammar)
    s_tokenized = str(s).split()
    parser = nltk.ChartParser(grammar)
    tree = list(parser.parse(s_tokenized))[:1]
    return tree

def funProgrammPassive(node: Tree) -> str:
    if type(node) is Tree:

        output = " "
        
        Sac = " ".join(node[0].leaves())
        Spa = " ".join(node[2].leaves())

        verb = Fem
        
        if node[2][0].label() != "Z":
            verb = Masc

        verbpas = verb[node[1][0]]

        output = f"{Spa} {verbpas} {Sac}"

        return output

        
if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
        tree = parse(s)
        if tree:
            salida = funProgrammPassive(tree[0])
        else:
            salida = "NO PERTENECE"
    except ValueError:
        salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()

