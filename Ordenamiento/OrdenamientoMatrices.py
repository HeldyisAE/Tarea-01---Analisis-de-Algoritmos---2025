"""
Se solicita la implementación de un algoritmo de ordenamiento para 
una lista de listas (matriz).
Se deben ordenar las listas dentro de la lista de manera independiente
de manera que cada lista dentro de la matriz esté ordenada.
"""

#Algoritmo quicksort para las listas
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    piv = lista[len(lista)//2] #seleccion de la mitad
    izq = [x for x in lista if x < piv] #elementos menores a piv
    mid = [x for x in lista if x == piv] #iguales a piv
    der = [x for x in lista if x > piv] #mayores a piv
    return quicksort(izq) + mid + quicksort(der)

#Función principal para iterar sobre cada lista en la matriz
def ordenarMatriz(matriz):
    for lista in range(len(matriz)): #Itera sobre las listas y da el indice para sobreescribir
        matriz[lista] = quicksort(matriz[lista]) 
    return matriz 

#ordenarMatriz([[1,2,3],[1,4,2],[6,9,5]])

"""
Se solicita la implementación de un algoritmo de ordenamiento distinto del anterior para 
realizar una comparación y analisis del rendimiento de los mismos
"""

#Algoritmo bubblesort de comparación
def bubblesort(lista):
    ultimo = len(lista) #Denota el final de la lista
    for i in range(ultimo):
        for j in range(ultimo - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] 
    return lista     

def comparacionOrdenamiento(matriz):
    #Se reutiliza de la función anterior
    for lista in range(len(matriz)): #Itera sobre las listas y da el indice para sobreescribir
        matriz[lista] = bubblesort(matriz[lista]) 

    return matriz 
#comparacionOrdenamiento([[3, 1, 5, 2, 4], [9, 6, 8, 5, 7], [12, 10, 15, 11, 14], [20, 18, 19, 17, 16], [25, 22, 21, 24, 23]])
