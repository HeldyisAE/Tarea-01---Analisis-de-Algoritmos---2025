import random

"""Es una función que recibe de entrada un numero y crea una matriz cuadrada con esa cantidad de filas y columnas 
    regresa la matriz con numeros aleatorios con un valor entre 1-999
"""

def crearM(n):
    if not isinstance(n,int):
        print("Error la entrada no fué un numero")
        return ""
    M=[]
    for x in range(n):
        temp=[]
        for x in range(n):
            temp.append(random.randint(1,1000))
        M.append(temp)
    
    return M

print(crearM(3))