"""
Dado un grafo no dirigido con personajes del MCU de la siguiente tabla:

personajes = ['Iron Man', 'The Incredible Hulk', 'Khan', 'Thor', 'Captain America', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']
conexiones = ([
  [0, 6, 0, 1, 8, 7, 3, 2],
  [6, 0, 0, 6, 1, 8, 9, 1],
  [0, 0, 0, 1, 2, 1, 5, 0],
  [1, 6, 1, 0, 1, 5, 9, 3],
  [8, 1, 2, 1, 0, 2, 4, 5],
  [7, 8, 1, 5, 2, 0, 1, 6],
  [3, 9, 5, 9, 4, 1, 0, 1],
  [2, 1, 0, 3, 5, 6, 1, 0]
])

Implementar los algoritmos necesarios para resolver las siguientes tareas:
 
- cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan;
 
- hallar el árbol de expansión máximo desde el vértice que contiene a Iron-Man, Thor y The Winter Soldier;
 
- determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con dicho número
 
- cargue todos los personajes de la tabla anterior
 
- indicar qué personajes aparecieron en nueve episodios de la saga.
"""


class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def agregar_arista(self, u, v, w):
        self.grafo.append([u, v, w])

    def buscar(self, parent, i):
        if parent[i] == i:
            return i
        return self.buscar(parent, parent[i])

    def unir(self, parent, rank, x, y):
        xroot = self.buscar(parent, x)
        yroot = self.buscar(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskalMST(self):
        result = []
        i, e = 0, 0
        self.grafo = sorted(self.grafo, key=lambda item: item[2], reverse=True)
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.buscar(parent, u)
            y = self.buscar(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.unir(parent, rank, x, y)

        return result


personajes = ['Iron Man', 'The Incredible Hulk', 'Khan', 'Thor', 'Captain America', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']
matriz = [
  [0, 6, 0, 1, 8, 7, 3, 2],
  [6, 0, 0, 6, 1, 8, 9, 1],
  [0, 0, 0, 1, 2, 1, 5, 0],
  [1, 6, 1, 0, 1, 5, 9, 3],
  [8, 1, 2, 1, 0, 2, 4, 5],
  [7, 8, 1, 5, 2, 0, 1, 6],
  [3, 9, 5, 9, 4, 1, 0, 1],
  [2, 1, 0, 3, 5, 6, 1, 0]
]

g = Grafo(len(personajes))

for i in range(len(matriz)):
    for j in range(i+1, len(matriz[i])):
        if matriz[i][j] != 0:
            g.agregar_arista(i, j, matriz[i][j])

mst = g.kruskalMST()


# if __name__ == "__main__":

print("Árbol de expansión máximo: ")
for u, v, w in mst:
    print(f"{personajes[u]} -- {personajes[v]} == {w}")

# Cargar todos los personajes
print("Personajes cargados:")
for personaje in personajes:
  print(personaje)

# Determinar cuál es el número máximo de episodios que comparten dos personajes
max_episodios = max(max(fila) for fila in matriz)
print(f"\nMáximo número de episodios compartidos: {max_episodios}")

# Indicar todos los pares de personajes que coinciden con dicho número
print("\nPares de personajes que comparten el máximo número de episodios:")
for i in range(len(matriz)):
  for j in range(i+1, len(matriz[i])):  # Solo necesitamos mirar la mitad superior de la matriz
    if matriz[i][j] == max_episodios:
      print(f"{personajes[i]} y {personajes[j]}")

# Indicar qué personajes aparecieron en nueve episodios de la saga
print("\nPersonajes que aparecieron en nueve episodios:")
for i in range(len(matriz)):
  if sum(matriz[i]) == 9:  # Sumar las apariciones de cada personaje
    print(personajes[i])
