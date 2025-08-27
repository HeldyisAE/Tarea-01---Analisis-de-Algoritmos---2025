"""
Archivo main para la ejecucuión del análisis de los diferentes
algoritmos implementados en este trabajo

Para el desarrollo de este archivo se utilizó ayuda leve de la IA ChatGPT
debido a la falta de experiencia con la librería tracenalloc y en 
modulación con Python
"""

import sys
import os
import time
import tracemalloc

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Búsqueda.BusquedaMatrices import busquedaLineal, busquedaMatriz
from Ordenamiento.OrdenamientoMatrices import quicksort, bubblesort
from CrearMatriz.matrizRandom import crearM

def probarOrdenamiento():
    tamaños = [100, 1000, 10000]
    for n in tamaños:
        matriz = crearM(n)
        for algoritmo in [bubblesort, quicksort]:
            temporal = [fila[:] for fila in matriz] #Linea hecha IA
            tracemalloc.start()
            inicio = time.time()
            for i, fila in enumerate(temporal):
                temporal[i] = algoritmo(fila) #Se agrega esta línea ya que quicksort no es in-place
            final = time.time()
            memoria = tracemalloc.get_traced_memory()[1] #Linea hecha con IA
            tracemalloc.stop()

            print(f"Para {algoritmo.__name__} con {n} elementos por fila: {final - inicio:.4f} s, {memoria/1024:.2f} KB")
            print(f"\n {temporal}")

def probarBusqueda(valor):
    tamaños = [10, 100, 500]
    for n in tamaños:
        matriz = crearM(n)
        
        for algoritmo in [busquedaMatriz, busquedaLineal]:
            tracemalloc.start()
            inicio = time.time()
            encontrado = algoritmo(matriz, valor)
            fin = time.time()
            memoria = tracemalloc.get_traced_memory()[1]
            tracemalloc.stop()

            print(f"Para {algoritmo.__name__} en {n}x{n}: {fin - inicio:.6f} s, {memoria/1024:.2f} KB, ¿Existe?={encontrado}")

if __name__ == "__main__":

    print("Pruebas de búsqueda:")
    probarBusqueda(4)

    print("\nPruebas de ordenamiento:")
    probarOrdenamiento()

    