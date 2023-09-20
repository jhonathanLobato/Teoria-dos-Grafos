import heapq

def astar(grafo, inicio, objetivo):
    lista_aberta = [(0, inicio)]
    veio_de = {} 
    custo_real = {no: float('inf') for no in grafo} 
    custo_real[inicio] = 0
    custo_total = {no: float('inf') for no in grafo}
    custo_total[inicio] = heuristica(inicio, objetivo)

    while lista_aberta:
        _, atual = heapq.heappop(lista_aberta)

        if atual == objetivo:
            return reconstruir_caminho(veio_de, atual)

        for vizinho, custo in grafo[atual]:
            custo_tentativo = custo_real[atual] + custo

            if custo_tentativo < custo_real[vizinho]:
                veio_de[vizinho] = atual
                custo_real[vizinho] = custo_tentativo
                custo_total[vizinho] = custo_tentativo + heuristica(vizinho, objetivo)
                heapq.heappush(lista_aberta, (custo_total[vizinho], vizinho))

    return None 

def heuristica(no, objetivo):
    x1, y1 = no
    x2, y2 = objetivo
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def reconstruir_caminho(veio_de, atual):
    caminho = [atual]
    while atual in veio_de:
        atual = veio_de[atual]
        caminho.append(atual)
    caminho.reverse()
    return caminho

grafo = {
    (0, 0): [((0, 1), 1), ((1, 0), 1)],
    (0, 1): [((0, 0), 1), ((1, 1), 1)],
    (1, 0): [((0, 0), 1), ((1, 1), 1)],
    (1, 1): [((0, 1), 1), ((1, 0), 1)]
}

inicio = (0, 0)
objetivo = (1, 1)

caminho = astar(grafo, inicio, objetivo)
print(caminho) 
