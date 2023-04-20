from parser import Process

def main():
    while True:
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
        option = int(input("Select the grammar for evaluate : "))
        g = ""
        if option == 1:
            g = grammar1
        elif option == 2:
            g = grammar2
        elif option == 3:
            g = grammar3
        elif option == 4:
            g = grammar4
        elif option == 5:
            g = grammar5
        else:
            print("Incorrect Option")
            continue 
        phrase = input("Enter the string: ")
        proc = Process(phrase, g)
        proc.validate()
        flag = (input("Continue ? y/n :"))
        if flag == 'n':
            break

if __name__ == "__main__":
    main()
    





