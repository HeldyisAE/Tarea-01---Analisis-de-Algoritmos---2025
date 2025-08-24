"""
Se solicita la implementación de un algoritmo de ordenamiento para 
una lista de listas (matriz).
Se deben ordenar las listas dentro de la lista de manera independiente
de manera que cada lista dentro de la matriz esté ordenada.
"""

#Algoritmo quicksort para las listas
def quicksort(lista):
    
    return

#Función principal para iterar sobre cada lista en la matriz
def ordenarMatriz(matriz):
    for lista in range(len(matriz)): #Itera sobre las listas y da el indice para sobreescribir
        matriz[lista] = quicksort(matriz[lista]) 
    return matriz 

ordenarMatriz([[1,2,3],[1,4,2],[6,9,5]])

