"""
Kamala Khan alias Ms. Marvel es una adolescente Musulmana Pakistaní-estadounidense de Nueva Jersey. En el MCU tiene un linaje mutante latente activado unos misteriosos 
anillos que le dan una polimorfa con la capacidad de estirar su cuerpo de casi cualquier forma imaginable. Kamala era una gran fan de los superhéroes, especialmente de 
Carol Danvers, la antigua Ms. Marvel y por eso se ha convertido en una experta en redes sociales, pero nos ha pedido ayuda para 
implementar un grafo social y los algoritmos necesarios para atender los siguientes requerimientos:

- cargar superhéroes de la siguiente tabla como vértices (puntos o nodos con los que están conformado los grafos. Llamaremos grado de un vértice, al número de aristas 
de las que es extremo) del grafo;

heroes = ['Iron Man', 'The Incredible Hulk', 'Khan', 'Thor', 'Captain America', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']

twitter_matrix = [
    [0, 75, 40, 16, 80, 20, 99, 23],
    [75, 0, 50, 67, 79, 38, 99, 41],
    [40, 50, 0, 17, 75, 52, 85, 28],
    [16, 67, 17, 0, 11, 50, 90, 36],
    [80, 79, 75, 11, 0, 26, 12, 56],
    [20, 38, 52, 50, 26, 0, 55, 61],
    [99, 99, 85, 90, 12, 55, 0, 10],
    [23, 41, 28, 36, 56, 61, 10, 0]
]

instagram_matrix = [
    [0, 61, 44, 66, 56, 74, 11, 65],
    [12, 0, 47, 41, 12, 38, 99, 41],
    [41, 23, 0, 45, 12, 89, 42, 14],
    [12, 69, 11, 0, 12, 50, 78, 63],
    [89, 19, 72, 11, 0, 26, 12, 56],
    [72, 34, 21, 65, 12, 0, 78, 41],
    [12, 87, 35, 99, 42, 15, 0, 10],
    [33, 41, 24, 61, 45, 41, 11, 0]
]

- cargar estos superhéroes con las siguientes etiquetas: Twitter, Instagram respectivamente, que representan si la persona del vértice origen sigue o es amigo de la persona 
del vértice destino;

- hallar el árbol de expansión máximo para cada red social (considere el grafo como no dirigido para este punto), es decir, que las conexiones deben ser las de mayor peso 
(ósea el que tenga mayor interacción); para lo cual, si desea utilizar Prim o Kruskal sin modificar el código, puede determinar la arista (relación entre dos vértices de un 
grafo) de mayor peso y cuando aplique este algoritmo, debe que considerar el peso de cada arista será la arista de mayor peso menos el peso de la arista;
 
- determine si es posible conectar la persona Capitana Marvel con Nick Fury a través de la red social Twitter;
 
- determine si es posible conectar la persona The Winter Soldier con Iron Man a través de cualquier red social;
 
- indique a todas las personas que sigue a través de su red de Instagram Thor.
"""

class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, nombre):
        if nombre not in self.vertices:
            self.vertices[nombre] = {}

    def agregar_arista(self, origen, destino, etiquetas):
        self.vertices[origen][destino] = etiquetas
    
    def arbol_expansion_maximo(self, plataforma):
        aristas = [(peso[plataforma], origen, destino) for origen, aristas in self.vertices.items() for destino, peso in aristas.items()]
        aristas.sort(reverse=True)  # Ordenamos las aristas en orden decreciente de peso
        arbol = Grafo()
        for heroe in self.vertices:
            arbol.agregar_vertice(heroe)
        conjuntos = {heroe: {heroe} for heroe in self.vertices}  # Un conjunto para cada nodo
        for peso, origen, destino in aristas:
            if destino not in conjuntos[origen]:  # Si los nodos no están ya conectados
                arbol.agregar_arista(origen, destino, {plataforma: peso})
                arbol.agregar_arista(destino, origen, {plataforma: peso})  # Como el grafo es no dirigido
                nuevo_conjunto = conjuntos[origen].union(conjuntos[destino])
                for nodo in nuevo_conjunto:
                    conjuntos[nodo] = nuevo_conjunto
        return arbol

    def existe_camino(self, inicio, fin):
        visitados = {inicio}
        pila = [inicio]
        while pila:
            nodo = pila.pop()
            if nodo == fin:
                return True
            for vecino in self.vertices[nodo]:
                if vecino not in visitados:
                    visitados.add(vecino)
                    pila.append(vecino)
        return False
    
    def seguidores(self, persona, plataforma):
        return [nombre for nombre, conexion in self.vertices[persona].items() if conexion[plataforma] > 0]
    
    def mas_popular(self, plataforma):
        max_interacciones = 0
        mas_popular = None
        for heroe, conexiones in self.vertices.items():
            interacciones = sum(conexion[plataforma] for conexion in conexiones.values())
            if interacciones > max_interacciones:
                max_interacciones = interacciones
                mas_popular = heroe
        return mas_popular
    
# Carga los datos
heroes = ['Iron Man', 'The Incredible Hulk', 'Khan', 'Thor', 'Captain America', 'Ant-Man', 'Nick Fury', 'The Winter Soldier']

twitter_matrix = [
    [0, 75, 40, 16, 80, 20, 99, 23],
    [75, 0, 50, 67, 79, 38, 99, 41],
    [40, 50, 0, 17, 75, 52, 85, 28],
    [16, 67, 17, 0, 11, 50, 90, 36],
    [80, 79, 75, 11, 0, 26, 12, 56],
    [20, 38, 52, 50, 26, 0, 55, 61],
    [99, 99, 85, 90, 12, 55, 0, 10],
    [23, 41, 28, 36, 56, 61, 10, 0]
]

instagram_matrix = [
    [0, 61, 44, 66, 56, 74, 11, 65],
    [12, 0, 47, 41, 12, 38, 99, 41],
    [41, 23, 0, 45, 12, 89, 42, 14],
    [12, 69, 11, 0, 12, 50, 78, 63],
    [89, 19, 72, 11, 0, 26, 12, 56],
    [72, 34, 21, 65, 12, 0, 78, 41],
    [12, 87, 35, 99, 42, 15, 0, 10],
    [33, 41, 24, 61, 45, 41, 11, 0]
]

# Crea el grafo
grafo = Grafo()


if __name__ == "__main__":

    # Añade los vértices y las aristas
    for i, heroe in enumerate(heroes):
        grafo.agregar_vertice(heroe)
        for j, otro_heroe in enumerate(heroes):
            if i != j:
                grafo.agregar_arista(heroe, otro_heroe, {"Twitter": twitter_matrix[i][j], "Instagram": instagram_matrix[i][j]})

    # Muestra el grafo
    for nombre, conexiones in grafo.vertices.items():
        print(f"{nombre}: {conexiones}")

    # Crea el árbol de expansión máximo para cada plataforma
    for plataforma in ["Twitter", "Instagram"]:
        arbol = grafo.arbol_expansion_maximo(plataforma)
        print(f"Árbol de expansión máximo para {plataforma}:")
        for nombre, conexiones in arbol.vertices.items():
            print(f"  {nombre}: {conexiones}")

    # Verifica si existe un camino entre 'Captain Marvel' y 'Nick Fury' en Twitter
    print("\n¿Existe un camino entre 'Captain Marvel' y 'Nick Fury' en Twitter?")
    print("Sí" if grafo.existe_camino('Captain America', 'Nick Fury') else "No")

    # Verifica si existe un camino entre 'The Winter Soldier' y 'Iron Man' en cualquier red social
    print("\n¿Existe un camino entre 'The Winter Soldier' y 'Iron Man' en cualquier red social?")
    print("Sí" if any(grafo.existe_camino('The Winter Soldier', 'Iron Man') for plataforma in ["Twitter", "Instagram"]) else "No")

    # Muestra a todas las personas que sigue Thor a través de Instagram
    print("\nPersonas que sigue Thor a través de Instagram:")
    for persona in grafo.seguidores('Thor', 'Instagram'):
        print(persona)

    # Encuentra el superhéroe más popular en cada plataforma
    for plataforma in ["Twitter", "Instagram"]:
        print(f"El superhéroe más popular en {plataforma} es {grafo.mas_popular(plataforma)}")