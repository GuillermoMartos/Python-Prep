from functools import reduce
import math

#Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

def isVocal(letter:str):
    """
    descript: take a letter and compare it with vocal lists, to determine if letter is/not vocal. No case sensitive.
    args: str
    return: true/false
    """
    
    vocals=["a","e","i","o","u"]
    if letter.lower() in vocals:
        return True
    else:
        return False
    

# print(isVocal("A"))

# Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

def sum(arr:list[int]):
    """
    descript: take list of int and sum all of them
    args: list of ints
    return: int as total sum value
    """
    
    n=reduce(lambda a,b:a+b, arr)
    return n

def multip(arr:list[int]):
    """
    descript: take list of int and multiplicate all of them
    args: list of ints
    return: int as total multiplicated value
    """
    
    n=reduce(lambda a,b:a*b, arr)
    return n

# print(sum([2,4,5]))
# print(multip([2,4,5]))


# Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(inv:str):
    """
    descript: inverse string chain
    args: single string 
    return: same string, inversed
    """
    
    return inv[::-1]

# print(inversa("hola!"))
# print(inversa("12345"))


# Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.

def es_palin(pal:str):
    """
    desc: receive str and check true/false for palindrome
    arg: str
    return: boolean for is palindrome
    """
    if pal==pal[::-1]:
        return True
    else:
        return False
    
# print(es_palin("hola"))
# print(es_palin("ollo"))
# print(es_palin("radar"))

# Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

def superposicion(list1:list, list2:list):
    """
    desc: take 2 lists and check if any item are in common
    arg: 2 lists of whtves
    return: boolean, if some item is in both lists
    """
    for i in range(0,len(list2)):
        n=filter(lambda a:a==list2[i], list1)
        if len(list(n))>0:
            return True
        if i==len(list2)-1:
            return False
        
        
# print(superposicion([1,2,3],[4,5,6]))
# print(superposicion([1,2,4],[4,5,6]))
# print(superposicion([1,2,7],[4,5,6]))
# print(superposicion([1,2,"4"],[4,5,6]))
# print(superposicion([1,2,"4"],["4",5,6]))


# Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".

def generar_n_caracteres(a:str,x:int):
    """
    desc:receive letter and int to multiplicate letter for int
    args: letter to multiplicate, int to indicate multiplication times for letter
    return: str of letter multiplicated
    """
    return a*x

# print(generar_n_caracteres("a",7))

# Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:*x4,*x9, *x7

def procedimiento(arr:list):
    """
    desc: receive list of int to return list of * multiplicated for each int in list
    arg: list of int
    return: list of * multiplicated
    """
    
    return list(map(lambda a:"*"*a, arr))

# print(procedimiento([7,8,2]))


