from grafos import Grafo


def bellmore_neuhauser(grafo):
    n = grafo.numVertices
    visitado = [False] * n
    tour = [0]
    visitado[0] = True

    while len(tour) < n:
        u = tour[-1]
        menor = float("inf")
        prox = -1

        for v in range(n):
            if not visitado[v] and 0 < grafo.matriz[u][v] < menor:
                menor = grafo.matriz[u][v]
                prox = v

        tour.append(prox)
        visitado[prox] = True

    tour.append(0)
    return tour


if __name__ == "__main__":
    g = Grafo(5)
    g.inserirAresta(0, 1, 10)
    g.inserirAresta(0, 4, 20)
    g.inserirAresta(1, 2, 35)
    g.inserirAresta(1, 3, 25)
    g.inserirAresta(1, 4, 30)
    g.inserirAresta(2, 3, 15)
    g.inserirAresta(3, 4, 30)

    tour = bellmore_neuhauser(g)
    print("Caminho Bellmore e Neuhauser:")
    print(" -> ".join(map(str, tour)))
