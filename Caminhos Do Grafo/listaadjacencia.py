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
    
    # Função comentada porque sim ora
    '''
    def ordem(self):
        print(f"Ordem: {self.num_vertices}")

    def tamanho(self):
        num_arestas = sum(len(vizinhos) for vizinhos in self.lista_adjacencia)
        if not self.direcionado:
            num_arestas //= 2
        print(f"Tamanho: {num_arestas}")

    # Ver o grau do grafo - Duas funções para tratar responsabilidades diferentes
    def grau(self):
        graus = [len(vizinhos) for vizinhos in self.lista_adjacencia]
        for x in range(len(self.lista_adjacencia)):
            print(f"Graus de {x}: {graus[x]}")

    # Ver o Vizinho do grafo - Tem duas funções pq sim
    def vizinhoSolo(self, no):
        vizinho = []
        for i in range(self.num_vertices):
            if i != no and i in self.lista_adjacencia[no]:
                vizinho.append(i)
        return vizinho
    def vizinhanca(self):
        vizinhos_dict = {}
        for no in range(self.num_vertices):
            vizinho = self.vizinhoSolo(no)
            vizinhos_dict[no] = vizinho        
            print(f"Vizinho de {no}: ",vizinhos_dict[no])
    '''
    
    # 1 - Mostrando os vertices visitados
    # Função para coringar ZEHAHAHAHA
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

    # 2 - Componentes desconexos
    # Pior dia da minha vida foi o dia em que eu quis fazer CC
    def verificar_desconexos(self):
        visitados = [False] * self.num_vertices
        num_desconexos = 0

        for vertice in range(self.num_vertices):
            if not visitados[vertice]:
                fila = deque([vertice])
                visitados[vertice] = True
                num_desconexos += 1

                while fila:
                    v = fila.popleft()
                    for vizinho in self.lista_adjacencia[v]:
                        if not visitados[vizinho]:
                            fila.append(vizinho)
                            visitados[vizinho] = True

        return num_desconexos - 1

    # 3 - Ordem Topologincan
    def ordem_topologica(self):
        if self.verificar_ciclico() == False and self.direcionado == True:
            grau_entrada = [0] * self.num_vertices

            # Calcula o grau de entrada de cada vértice
            for vizinhos in self.lista_adjacencia:
                for vizinho in vizinhos:
                    grau_entrada[vizinho] += 1
            fila = deque()

            # Inicializa a fila com vértices de grau de entrada zero
            for vertice in range(self.num_vertices):
                if grau_entrada[vertice] == 0:
                    fila.append(vertice)
            ordem_topologica = []

            while fila:
                vertice = fila.popleft()
                ordem_topologica.append(vertice)
                for vizinho in self.lista_adjacencia[vertice]:
                    grau_entrada[vizinho] -= 1
                    if grau_entrada[vizinho] == 0:
                        fila.append(vizinho)

            print("Ordem Topológica:", ordem_topologica)
        else:
            print('O grafo é ciclico e/ou não é direcionado, por isso não existe topologia')

    # 4 - É ciclico ou não é? A laaranja tem citrica?
    def verificar_ciclico(self):
        visitados = np.zeros(self.num_vertices, dtype=bool)

        def tem_ciclo(vertice, pai):
            visitados[vertice] = True

            for vizinho in self.lista_adjacencia[vertice]:
                if not visitados[vizinho]:
                    if tem_ciclo(vizinho, vertice):
                        return True
                elif vizinho != pai:
                    return True
            return False

        for vertice in range(self.num_vertices):
            if not visitados[vertice]:
                if tem_ciclo(vertice, -1):
                    return True
        return False


if __name__ == '__main__':
    # De volta outra vez...
    lista_bfs = Grafo(6)
    lista_bfs.adicionar_aresta(0, 1)
    lista_bfs.adicionar_aresta(1, 3)
    #lista_bfs.adicionar_aresta(1, 2)
    lista_bfs.adicionar_aresta(2, 4)
    lista_bfs.adicionar_aresta(4, 5)
    lista_bfs.adicionar_aresta(5, 2)
    
    # Imprimindo a lista de adjacência
    lista_bfs.imprimir_lista_adjacencia()
    '''
    lista_bfs.ordem()
    lista_bfs.tamanho()
    lista_bfs.grau()
    lista_bfs.vizinhanca()
    '''
    print()
    print("** BUSCA EM LARGURA **")
    print()

    # 1
    print("Busca em Largura a partir do vértice: ")
    busca = lista_bfs.busca_em_largura(3)
    print()

    # 2
    num_desconexos = lista_bfs.verificar_desconexos()
    print(f"Número de componentes desconexos: {num_desconexos}")
    print()

    # 3
    lista_bfs.ordem_topologica()
    print()

    # 4
    if lista_bfs.verificar_ciclico():
        print("O grafo é ciclico")
    else:
        print("O grafo é aciclico")
        

