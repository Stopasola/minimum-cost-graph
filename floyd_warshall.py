import time
import copy
import sys


INF = sys.maxsize


def floyd_warshall(graph_size, dist):

    for k in range(graph_size): # 2n+1

        for i in range(graph_size): # 2n^2+ 1n

            for j in range(graph_size): # 2n^3+ 1n^2

                if i == j:      # 1n^3 rela
                    dist[i][j] = 0  # 1n^3 atrin + # 2n^3 indexa
                else:
                    # 1n^3 atrib +  8n^3 indexa + custo func min + 1n^3 arit
                    dist[i][j] = min(dist[i][j], (dist[i][k] + dist[k][j]))

    return dist # 1 op


def print_solution(dist, graph_size):

    print("Matriz Distancias Floyd Warshall:")

    for i in range(graph_size):
        for j in range(graph_size):
            if dist[i][j] == INF:
                print("%7s" % "0", end="")
            else:
                print("%7d\t" % (dist[i][j]), end="")
            if j == graph_size - 1:
                print("")


def operation_fw(graph_size, graph_matrix, print_results):

    edited_graph_matrix = copy.deepcopy(graph_matrix)

    # changing notation
    for i in range(0, graph_size):
        for j in range(0, graph_size):
            if edited_graph_matrix[i][j] == 0:
                edited_graph_matrix[i][j] = INF

    # Running algorithm
    start_time = time.time()
    dist = floyd_warshall(graph_size, edited_graph_matrix)
    elapsed_time = time.time() - start_time

    if print_results:
        print_solution(dist, graph_size)

    return round(elapsed_time, 5)
