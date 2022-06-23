 # -*- coding: utf-8 -*-

import sys
import io
import nltk
from nltk.tree import Tree


class Node(object):
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

    def addIzq(self,dato):
        self.izq=dato

    def addDer(self,dato):
        self.der=dato

    def addDato(self,dato):
        self.dato=dato

def obtenerParte(entry):
    output=[]
    if (entry[0]=='('):
        cantidadParentesis=1
        output=['(']
        iterator=1;
        while (cantidadParentesis>0):
            output.append(entry[iterator])
            if (entry[iterator]==')'):
                cantidadParentesis=cantidadParentesis-1
            elif (entry[iterator]=='('):
                cantidadParentesis=cantidadParentesis+1
            iterator=iterator+1
        output.pop()
        output.pop(0)
        for i in range(0,iterator):
            entry.pop(0)
    elif(entry[0]!='not'):
        output.append(entry[0])
        entry.pop(0)
    elif(entry[0]=='not'):
        for i in range(0,len(entry)):
            output.append(entry[0])
            entry.pop(0)
    return output

def construirArbol(entry):
    if (len(entry)==1):
        resultado=Node(entry)
        resultado.addIzq(None)
        resultado.addDer(None)
        resultado.addDato(entry[0])
        entry.pop(0)
        return resultado
    elif (len(entry)>1):
        resultado=Node(entry)
        if (entry[0]!='not'):
            a=obtenerParte(entry)
            resultado.addIzq(construirArbol(a))
            resultado.addDato(entry[0])
            entry.pop(0)
            b = obtenerParte(entry)
            resultado.addDer(construirArbol(b))
        elif(entry[0]=='not'):
            resultado.addDato(entry[0])
            entry.pop(0)
            a=obtenerParte(entry)
            resultado.addIzq(construirArbol(a))
            resultado.addDer(None)
        return resultado

def imprimirArbol(tree,nivel):
    if (tree is not None):
        cadena=''
        if (tree.dato=='and' or tree.dato=='or'):
            cadena=cadena + tree.dato + '(' + imprimirArbol(tree.izq,nivel +1) +','+ imprimirArbol(tree.der,nivel +1) + ')'
        elif (tree.dato=='not'):
            cadena=cadena + tree.dato + '(' + imprimirArbol(tree.izq,nivel +1) + ')'
        else:
            cadena=cadena + tree.dato
        return cadena
    else:
        cadena=''
        return cadena


def parse(s):
    splitStrin = s.split()
    grammar = """
    S -> 'not' S | S 'and' S | S 'or' S | A | '(' S ')'
    A -> 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z'
    """
    grammar = nltk.CFG.fromstring(grammar)
    parser = nltk.LeftCornerChartParser(grammar)
    tree = list(parser.parse(splitStrin))[:1]
    return tree

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s)
      if tree:
          res = construirArbol(s.split())
          salida = imprimirArbol(res, 0)
      else:
          salida = "NO PERTENECE"
    except ValueError:
      salida = "NO CUBRE"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()

