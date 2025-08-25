"""
Se solicita la implementación de un algoritmo de búsqueda para 
una lista de listas (matriz).
Se debe buscar un valor en las listas dentro de la lista de manera independiente
"""


#Algoritmo de búsqueda binaria para las listas
def busquedaBinaria(lista, valor):
    
    found = True
    
    return found

#Algoritmo principal de iteración sobre cada lista de la matrizl
def busquedaMatriz(matriz, valor):
    resultado = False
    for lista in matriz:
        if busquedaBinaria(lista, valor):
            resultado = True
            break
    
    return resultado

#busquedaMatriz([[1,2,3],[1,4,2],[6,9,5]], 4)



"""
Se solicita la implemetación de un algoritmo de búsqueda distinto del anterior
para realizar la comparación y anánilisis de sus rendimientos
"""


#Algoritmo de búsqueda lineal
def busquedaLineal(matriz, valor):
    encontrado = False
    for i in matriz:
        for j in i:
            if j == valor:
                encontrado = True
    print(encontrado)
    return encontrado

busquedaLineal([[1, "a", "sol", 9, "x"], ["gato", 15, "m", "python", 3], ["casa", "r", 7, "luz", "d"], ["f", 22, "t", "j", "libro"], [8, "v", "w", "amigo", "paz"]], 1)