import heapq

def dijkstra(grafo, inicio):
    n = grafo.ordem()
    inicio_idx = inicio - 1
    
    distancias = [float('inf')] * n
    distancias[inicio_idx] = 0.0
    
    antecessores = [-1] * n
    
    pq = [(0.0, inicio_idx)]
    
    while pq:
        distAtual, u = heapq.heappop(pq)
        
        if distAtual > distancias[u]:
            continue
            
        for v in range(n):
            peso = grafo.matriz[u][v]
            if peso > 0:
                if distancias[u] + peso < distancias[v]:
                    distancias[v] = distancias[u] + peso
                    antecessores[v] = u
                    heapq.heappush(pq, (distancias[v], v))

    caminhos = {}
    for i in range(n):
        if distancias[i] == float('inf'):
            caminhos[i + 1] = []
        else:
            caminho = []
            atual = i
            while atual != -1:
                caminho.append(atual + 1)
                atual = antecessores[atual]
            caminho.reverse()
            caminhos[i + 1] = caminho
            
    dist_dict = {i + 1: distancias[i] for i in range(n)}
    
    return dist_dict, caminhos