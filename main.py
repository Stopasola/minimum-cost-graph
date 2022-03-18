import csv
from dijkstra import operation_djk
from floyd_warshall import operation_fw


def graph_density(graph_matrix):

    edge = 0
    for i in range(0, graph_size):
        for j in range(0, graph_size):
            if graph_matrix[i][j] != 0:
                edge += 1
    p = edge/(graph_size * (graph_size - 1))
    if p < 1:
        return 'sparse'
    else:
        return 'dense'


def write_csv(graph_time):
    with open('GraficoTempo.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=';')
        spamwriter.writerow(['Arq', 'Tempo_Dijkstra', 'Tempo_Floyd_Warshall'])
        for k in range(0, len(graph_time)):
            spamwriter.writerow([graph_time[k][0], graph_time[k][1], graph_time[k][2]])



vetorArquivo = [10, 25, 50, 75, 100, 150, 200, 250, 300, 400, 500, 650, 800, 1000, 1500]

graph_matrix = list()
graph_time = list()
print_results = False
output_csv = False

for i in range(0, len(vetorArquivo)):

    # File Name
    data_file = 'dataset/Entrada ' + str(vetorArquivo[i]) + '.txt'

    # Open File
    open_data_file = open(data_file, 'r')
    graph_size = int(open_data_file.readline())
    for j in range(0, graph_size):
        graph_line = open_data_file.readline()
        graph_line = graph_line.split(' ')
        graph_line = graph_line[:-1]
        graph_line = list(map(int, graph_line))
        graph_matrix.append(graph_line)

    open_data_file.close()

    #  Call Dijkstra script
    dijkstra_elapsed_time = operation_djk(graph_size, graph_matrix, print_results)

    #  Call Floyd_Warshall script
    floyd_elapsed_time = operation_fw(graph_size, graph_matrix, print_results)

    # Add grafic structure
    file_name = str('Arq' + str(vetorArquivo[i]))
    graph_time.append([file_name, str(dijkstra_elapsed_time), str(floyd_elapsed_time)])

    # Save in csv file
    if output_csv
        write_csv(graph_time) 

    # discovery graph density
    density = graph_density(graph_matrix)

    # print results
    print('----------------------------------------------')
    print('graph_density', density)
    print('graph_size', graph_size)
    print('graph_matrix', graph_matrix)
    print('dijkstra_elapsed_time', dijkstra_elapsed_time)
    print('floyd_elapsed_time', floyd_elapsed_time)
    print('graph_time', graph_time)

    graph_matrix.clear()



