class Grafo:

    def __init__(self, arquivo):
        self.matriz = []
        self.ordem_grafo = 0

        self.ler_grafo(arquivo)

    def ler_grafo(self, arquivo):
        with open(arquivo, "r") as f:
            linhas = f.readlines()

        self.ordem_grafo = int(linhas[0])

        self.matriz = [
            [0] * self.ordem_grafo
            for _ in range(self.ordem_grafo)
        ]

        for linha in linhas[1:]:
            v1, v2, peso = linha.split()

            v1 = int(v1)
            v2 = int(v2)
            peso = float(peso)

            self.matriz[v1 - 1][v2 - 1] = peso
            self.matriz[v2 - 1][v1 - 1] = peso

    def ordem(self):
        return self.ordem_grafo

    def tamanho(self):
        quantidade = 0

        for i in range(self.ordem_grafo):
            for j in range(i + 1, self.ordem_grafo):
                if self.matriz[i][j] != 0:
                    quantidade += 1

        return quantidade

    def densidade(self):
        n = self.ordem()
        m = self.tamanho()

        if n <= 1:
            return 0

        return (2 * m) / (n * (n - 1))

    def vizinhos(self, vertice):
        vizinhos = []

        for j in range(self.ordem_grafo):
            if self.matriz[vertice - 1][j] != 0:
                vizinhos.append(j + 1)

        return vizinhos

    def grau(self, vertice):
        return len(self.vizinhos(vertice))

    def _dfs_sem_vertice(self, atual, removido, visitados):
        visitados[atual] = True

        for vizinho in range(self.ordem_grafo):
            if vizinho == removido:
                continue

            if self.matriz[atual][vizinho] != 0 and not visitados[vizinho]:
                self._dfs_sem_vertice(vizinho, removido, visitados)

    