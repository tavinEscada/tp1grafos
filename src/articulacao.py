from src.grafo import Grafo


def dfs(grafo, u, visitados, pai, profundidade, low, articulacoes, tempo):

    visitados[u] = True

    profundidade[u] = tempo[0]
    low[u] = tempo[0]

    tempo[0] += 1

    filhos = 0

    for v in range(grafo.ordem()):

        if grafo.matriz[u][v] == 0:
            continue

        if not visitados[v]:

            pai[v] = u
            filhos += 1

            dfs(
                grafo,
                v,
                visitados,
                pai,
                profundidade,
                low,
                articulacoes,
                tempo
            )

            low[u] = min(low[u], low[v])

            if pai[u] == -1 and filhos > 1:
                articulacoes.add(u)

            if pai[u] != -1 and low[v] >= profundidade[u]:
                articulacoes.add(u)

        elif v != pai[u]:

            low[u] = min(low[u], profundidade[v])


def encontra_articulacao(grafo):

    visitados = [False] * grafo.ordem()
    pai = [-1] * grafo.ordem()
    profundidade = [-1] * grafo.ordem()
    low = [-1] * grafo.ordem()

    articulacoes = set()
    tempo = [0]

    for i in range(grafo.ordem()):

        if not visitados[i]:

            dfs(
                grafo,
                i,
                visitados,
                pai,
                profundidade,
                low,
                articulacoes,
                tempo
            )

    return {vertice + 1 for vertice in articulacoes}

def eh_articulacao(grafo, vertice):

    articulacoes = encontra_articulacao(grafo)

    return vertice in articulacoes