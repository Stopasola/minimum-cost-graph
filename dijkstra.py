import sys
import time

matrix_path = list()


class Graph:

    def __init__(self, vertices):
        self.V = vertices

    def printSolution(self, dist):
        matrix_line = list()
        for node in range(self.V):
            matrix_line.append(dist[node])
        matrix_path.append(matrix_line[:])
        matrix_line.clear()

    def minDistance(self, dist, sptSet):
        min = sys.maxsize                           # 1n atribuições
        for v in range(self.V):                     # (2n + 1)n
            if dist[v] < min and not sptSet[v]:     # 2n^2 indexações + 2n^2 op Lógicas + 1n^2 op relacional
                min = dist[v]                       # 1n^2 atribuição + 1n^2 indexação
                min_index = v                       # 1n^2 atribuição
        return min_index                            # 1n op

    def dijkstra(self, src, print_results):
        dist = [sys.maxsize] * self.V               # n indexações na lista
        dist[src] = 0                               # 1 indexação + 1 atribuição
        sptSet = [False] * self.V                   # n indexações na lista

        for cout in range(self.V):                  # 2 n + 1

            u = self.minDistance(dist, sptSet)      # Analise da função linha 19
            sptSet[u] = True                        # n indexações

            for v in range(self.V):                 # 2 n^2 + 1n
                # 5n^2 indexações + 2n^2 op relacional + 2n^2 arit + 2n^2 logi
                if self.graph[u][v] > 0 and sptSet[v] == False\
                        and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]     # 1n^2 op atrib + 1n^2 op arit + 4n^2 indexação

        if print_results:
            self.printSolution(dist)


def print_solution_matrix(graph_size):
    print("Matriz Distancias Dijkstra:")
    for i in range(graph_size):
        for j in range(graph_size):
            print("%7d\t" % (matrix_path[i][j]), end="")
        print("")


def operation_djk(graph_size, graph_matrix, print_results):
    g = Graph(graph_size)
    g.graph = graph_matrix

    start_time = time.time()

    for i in range(0, graph_size):
        g.dijkstra(i, print_results)

    elapsed_time = time.time() - start_time

    if print_results:
        print_solution_matrix(graph_size)

    return round(elapsed_time, 5)
