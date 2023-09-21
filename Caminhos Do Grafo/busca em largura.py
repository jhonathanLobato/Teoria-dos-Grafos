import numpy as np
from collections import deque

class Grafo:
    def __init__(self, num_vertices, direcionado=False):
        self.num_vertices = num_vertices
        self.direcionado = direcionado
        self.lista_adjacencia = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, u, v):
        self.lista_adjacencia[u].append(v)
        if not self.direcionado:
            self.lista_adjacencia[v].append(u)

    def imprimir_lista_adjacencia(self):
        for vertice, vizinhos in enumerate(self.lista_adjacencia):
            print(f"{vertice} -> {vizinhos}")
    
    def busca_em_largura(self, inicio):
        visitados = [False] * self.num_vertices
        fila = deque([inicio])
    
        while fila:
            vertice = fila.popleft()
            if not visitados[vertice]:
                print(vertice, end=" ")
                visitados[vertice] = True
    
                for vizinho in self.lista_adjacencia[vertice]:
                    if not visitados[vizinho]:
                        fila.append(vizinho)
        print()

if __name__ == '__main__':
    lista_bfs = Grafo(6)
    lista_bfs.adicionar_aresta(0, 1)
    lista_bfs.adicionar_aresta(1, 3)
    lista_bfs.adicionar_aresta(1, 2)
    lista_bfs.adicionar_aresta(2, 4)
    lista_bfs.adicionar_aresta(4, 5)
    
    lista_bfs.imprimir_lista_adjacencia()

    print()
    print("** BUSCA EM LARGURA **")
    print()

    # 1
    print("Busca em Largura a partir do vértice: ")
    busca = lista_bfs.busca_em_largura(3)
    print()
