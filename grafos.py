import numpy as np


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz = [[0] * vertices for _ in range(vertices)]
        self.lista = [[] for _ in range(vertices)]

    def adicionar_aresta_matriz(self, u, v):
        # Adiciona uma aresta (u, v) na matriz de adjacência.
        self.matriz[u][v] = 1
        self.matriz[v][u] = 1  # Para grafos não direcionados

    def adicionar_aresta_lista(self, u, v):
        # Adiciona uma aresta (u, v) na lista de adjacência.
        self.lista[u].append(v)
        self.lista[v].append(u)  # Para grafos não direcionados

    def grau_vertice_matriz(self, vertice):
        # Calcula o grau de um vértice usando a matriz de adjacência.
        grau = 0
        for i in range(self.vertices):
            if self.matriz[vertice][i] == 1:
                grau += 1
        return grau

    def grau_vertice_lista(self, vertice):
        # Calcula o grau de um vértice usando a lista de adjacência.
        return len(self.lista[vertice])

    def imprimir_matriz(self):
        # Imprime a matriz de adjacência.
        for linha in self.matriz:
            print(linha)

    def imprimir_lista(self):
        # Imprime a lista de adjacência.
        for i, vizinhos in enumerate(self.lista):
            print(f"Vértice {i}: {vizinhos}")


# Exemplo de uso
g_matriz = Grafo(5)
g_matriz.adicionar_aresta_matriz(0, 1)
g_matriz.adicionar_aresta_matriz(0, 4)
g_matriz.adicionar_aresta_matriz(1, 2)
g_matriz.adicionar_aresta_matriz(1, 3)
g_matriz.adicionar_aresta_matriz(1, 4)
g_matriz.adicionar_aresta_matriz(2, 3)
g_matriz.adicionar_aresta_matriz(3, 4)

g_lista = Grafo(5)
g_lista.adicionar_aresta_lista(0, 1)
g_lista.adicionar_aresta_lista(0, 4)
g_lista.adicionar_aresta_lista(1, 2)
g_lista.adicionar_aresta_lista(1, 3)
g_lista.adicionar_aresta_lista(1, 4)
g_lista.adicionar_aresta_lista(2, 3)
g_lista.adicionar_aresta_lista(3, 4)

print("Matriz de Adjacência:")
g_matriz.imprimir_matriz()
print(f"Grau do vértice 1 (matriz): {g_matriz.grau_vertice_matriz(1)}")

print("\nLista de Adjacência:")
g_lista.imprimir_lista()
print(f"Grau do vértice 1 (lista): {g_lista.grau_vertice_lista(1)}")
