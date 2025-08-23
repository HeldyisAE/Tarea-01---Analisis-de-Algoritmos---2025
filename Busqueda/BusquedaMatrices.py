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

busquedaMatriz([[1,2,3],[1,4,2],[6,9,5]], 4)
