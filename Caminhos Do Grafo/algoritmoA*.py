import heapq

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}
    
    def adicionar_vertice(self, vertice):
        self.vertices.add(vertice)
        if vertice not in self.arestas:
            self.arestas[vertice] = []
    
    def adicionar_aresta(self, origem, destino, custo):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.arestas[origem].append((destino, custo))
        self.arestas[destino].append((origem, custo))

def a_estrela(grafo, inicio, objetivo):
    fila_prioridade = [(0, inicio)]
    custos = {vertice: float('inf') for vertice in grafo.vertices}
    custos[inicio] = 0
    pai = {}

    while fila_prioridade:
        _, atual = heapq.heappop(fila_prioridade)

        if atual == objetivo:
            caminho = []
            while atual in pai:
                caminho.append(atual)
                atual = pai[atual]
            caminho.append(inicio)
            return list(reversed(caminho))

        for vizinho, custo in grafo.arestas[atual]:
            novo_custo = custos[atual] + custo

            if novo_custo < custos[vizinho]:
                custos[vizinho] = novo_custo
                prioridade = novo_custo + heuristica(vizinho, objetivo)
                heapq.heappush(fila_prioridade, (prioridade, vizinho))
                pai[vizinho] = atual

    return None

def heuristica(origem, objetivo):
    # Esta é uma heurística simples, a distância em linha reta entre as cidades (não geograficamente precisa).
    return abs(ord(origem) - ord(objetivo))

# Exemplo de uso
grafo = Grafo()
grafo.adicionar_aresta('A', 'B', 5)
grafo.adicionar_aresta('A', 'C', 3)
grafo.adicionar_aresta('B', 'D', 2)
grafo.adicionar_aresta('C', 'D', 7)
grafo.adicionar_aresta('C', 'E', 8)
grafo.adicionar_aresta('D', 'E', 1)
grafo.adicionar_aresta('B', 'F', 4)
grafo.adicionar_aresta('E', 'F', 6)

inicio = 'A'
objetivo = 'E'

caminho = a_estrela(grafo, inicio, objetivo)

if caminho:
    print("Caminho encontrado:", caminho)
else:
    print("Não foi possível encontrar um caminho.")
caminho = a_estrela(grafo, inicio, objetivo)
print(caminho) 
