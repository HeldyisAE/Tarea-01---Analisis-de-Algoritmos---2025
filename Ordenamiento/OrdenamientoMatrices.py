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
def ejecutarQuicksort(matriz):
    for lista in range(len(matriz)): #Itera sobre las listas y da el indice para sobreescribir
        matriz[lista] = quicksort(matriz[lista]) 
    return matriz 

"""
Sentencias de ejecución, eliminar '#' para utilizar
"""

#QSOrdenada = ejecutarQuicksort([[1,2,3],[1,4,2],[6,9,5]])
#print(QSOrdenada)

"""
Se solicita la implementación de un algoritmo de ordenamiento distinto del anterior para 
realizar una comparación y analisis del rendimiento de los mismos
"""

#Algoritmo bubblesort de comparación
#Para esta implementación se utilizó ayuda de la IA Copilot y ChatGPT 
#Para entender y corregir errores, además de utilizar métodos que no se conocían
def mergesort(lista):
    if len(lista) <= 1: # En caso de lista con 1 o menos elementos
        return lista #Denota el final de la lista
    medio = len(lista) // 2
    izq = mergesort(lista[:medio])
    der = mergesort(lista[medio:])
    return merge(izq, der)

def merge(izq, der):
    resultado = []
    i = j = 0 #Doble asignación
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])  
            j += 1
    resultado.extend(izq[i:])   
    resultado.extend(der[j:])
    return resultado

def ejecutarMergesort(matriz):
    #Se reutiliza de la función anterior
    for lista in range(len(matriz)): #Itera sobre las listas y da el indice para sobreescribir
        matriz[lista] = mergesort(matriz[lista]) 

    return matriz 

"""
Sentencias de ejecución, eliminar '#' para utilizar
"""

#BSOrdenada = ejecutarMergesort([[3, 1, 5, 2, 4], [9, 6, 8, 5, 7], [12, 10, 15, 11, 14], [20, 18, 19, 17, 16], [25, 22, 21, 24, 23]])
#print(BSOrdenada)
