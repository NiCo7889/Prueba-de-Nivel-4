"""
Nick Fury se encuentra en los cuarteles generales de S.H.I.E.L.D. y debe visitar a varios superhéroes para convencerlos de unirse para formar un grupo de vengadores, 
dado que es un asunto de suma importancia nos solicita 
implementar un algoritmo que permita determinar el recorrido de menor distancia (el menor posible, no importa que 
sea el óptimo) y terminar dicho recorrido de vuelta en los cuarteles (solo se puede pasar una vez por cada lugar).
 
- Considere los siguientes superhéroes: S.H.I.E.L.D.

heroes = ["Iron Man", "The Incredible Hulk", "Khan", "Thor", "Captain America", "Ant-Man", "Nick Fury", "The Winter Soldier"]

- las distancias entre la localización de cada superhéroe están cargadas en la siguiente matriz:

distancias = [
    [0, 675, 400, 166, 809, 720, 399, 233],
    [675, 0, 540, 687, 179, 348, 199, 401],
    [400, 540, 0, 107, 752, 521, 385, 280],
    [166, 687, 107, 0, 111, 540, 990, 361],
    [809, 179, 752, 111, 0, 206, 412, 576],
    [720, 348, 521, 540, 206, 0, 155, 621],
    [399, 199, 385, 990, 412, 155, 0, 100],
    [233, 401, 280, 361, 576, 621, 100, 0]
]
"""


# Esta solución tiene una complejidad de tiempo O(n^2 * 2^n), lo que la hace factible para hasta alrededor de 20-25 ciudades.

import numpy as np

# Definimos la función de viaje recursiva
def travel(distancias, mascaras, nodo, mascara):
    # Si ya hemos calculado esta instancia del problema, la retornamos
    if mascaras[nodo][mascara] != -1:
        return mascaras[nodo][mascara]
    
    # Si todos los nodos han sido visitados, retornamos la distancia al nodo inicial
    if mascara == ((1<<len(distancias)) - 1):
        return distancias[nodo][0]
    
    min_distancia = np.inf
    # Probamos todas las ciudades restantes
    for i in range(len(distancias)):
        if (mascara>>i) & 1 == 0:
            min_distancia = min(min_distancia, distancias[nodo][i] + travel(distancias, mascaras, i, mascara|(1<<i)))
    
    # Almacenamos la solución al problema para uso futuro
    mascaras[nodo][mascara] = min_distancia
    return min_distancia

# Definimos la función TSP
def TSP(distancias):
    n = len(distancias)
    # Inicializamos las mascaras en -1
    mascaras = [[-1]*(1<<n) for _ in range(n)]
    
    # Llamamos a la función de viaje recursiva
    return travel(distancias, mascaras, 0, 1)

heroes = ["Iron Man", "The Incredible Hulk", "Khan", "Thor", "Captain America", "Ant-Man", "Nick Fury", "The Winter Soldier"]

distancias = np.array([
    [0, 675, 400, 166, 809, 720, 399, 233],
    [675, 0, 540, 687, 179, 348, 199, 401],
    [400, 540, 0, 107, 752, 521, 385, 280],
    [166, 687, 107, 0, 111, 540, 990, 361],
    [809, 179, 752, 111, 0, 206, 412, 576],
    [720, 348, 521, 540, 206, 0, 155, 621],
    [399, 199, 385, 990, 412, 155, 0, 100],
    [233, 401, 280, 361, 576, 621, 100, 0]
])


if __name__ == "__main__":

    print("La distancia mínima es: ", TSP(distancias))
