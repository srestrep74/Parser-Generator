# Parser-Generator

## Hecho por :
Sebastian Restrepo Ortiz

## Gramaticas que reciben el programa :

        grammar1 = """ 
                    A -> 'a' B F
                    F -> 'd' F |
                    B -> 'b'
                    """
        grammar2 = """ 
                    S -> A 'a' A 'b' | B 'b' B 'a'
                    A -> |
                    B -> |
                    """
        grammar3 = """ 
                    E -> E '+' T | T
                    T -> T 'x' F | F
                    F -> '(' E ')' | 'id'
                    """
        grammar4 = """ 
                    E -> T H
                    H -> '+' T H |
                    T -> F I
                    I -> 'x' F I |
                    F -> '(' E ')' | 'id'
                    """
        grammar5 = """ 
                    S -> A C B | C 'b' b | B 'a'
                    A -> 'da' | B C
                    B -> 'g' |
                    C -> 'h' |
                    """
                   
Dentro de esta sintaxis, cada no-terminal se sigue representando mediante una letra mayuscula, y cada no terminal debe de ir entre llaves simples. Ademas, hay que tener en cuenta que cada posible produccion, esta separada por '|' y si hay un luego de un '|' no hay nada , significa que va un epsilon.

## Forma de ingresar la cadena:

Como ejemplo, suponga que la gramatica es :

    grammar1 = """ 
                    A -> 'a' B F
                    F -> 'd' F |
                    B -> 'b'
                    """

Esta gramatica acepta la cadena 'abddd' por ejemplo. A la hora de ingresar esta cadena para validarla con el programa, se debe de ingresar cada caracter separado por un espacio. Es decir, en lugar de ingresar 'abddd', se debe de ingresar 'a b d d d'.
        
