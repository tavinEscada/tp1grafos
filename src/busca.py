from collections import deque

def busca_largura(grafo, inicio):

    n = grafo.ordem()

    if inicio < 1 or inicio > n:
        return [], []

    visitados = [False] * n
    fila = deque()
    ordem = []
    arestas_arvore = set()

    inicio = inicio - 1

    visitados[inicio] = True
    fila.append(inicio)

    while fila:

        atual = fila.popleft()
        ordem.append(atual + 1)

        for vizinho in range(n):

            if grafo.matriz[atual][vizinho] != 0:

                if not visitados[vizinho]:

                    visitados[vizinho] = True
                    fila.append(vizinho)

                    aresta = tuple(sorted((atual, vizinho)))
                    arestas_arvore.add(aresta)

    fora_arvore = []

    for i in range(n):

        for j in range(i + 1, n):

            if grafo.matriz[i][j] != 0:

                aresta = (i, j)

                if aresta not in arestas_arvore:
                    fora_arvore.append((i + 1, j + 1))

    return ordem, fora_arvore


def componentes_conexas(grafo):

    n = grafo.ordem()

    visitados = [False] * n
    componentes = []

    for inicio in range(n):

        if not visitados[inicio]:

            fila = deque()
            componente = []

            visitados[inicio] = True
            fila.append(inicio)

            while fila:

                atual = fila.popleft()
                componente.append(atual + 1)

                for vizinho in range(n):

                    if grafo.matriz[atual][vizinho] != 0:

                        if not visitados[vizinho]:

                            visitados[vizinho] = True
                            fila.append(vizinho)

            componentes.append(componente)

    return componentes


def possui_ciclo(grafo):

    n = grafo.ordem()

    visitados = [False] * n

    for inicio in range(n):

        if not visitados[inicio]:

            fila = deque()

            visitados[inicio] = True
            fila.append((inicio, -1))

            while fila:

                atual, pai = fila.popleft()

                for vizinho in range(n):

                    if grafo.matriz[atual][vizinho] != 0:

                        if not visitados[vizinho]:

                            visitados[vizinho] = True
                            fila.append((vizinho, atual))

                        elif vizinho != pai:

                            return True

    return False