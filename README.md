# Dijkstra and Floyd-Warshall algorithms comparison sekking minimum cost 

![image](https://img.shields.io/github/languages/top/stopasola/minimum-cost-graph)


## Introduction

In this work was analyzed the chronological performance spent in distance for a given set of graphs, implementing Dijkstra and Floyd-Warshall algorithms. Beyond chronological time analysis, the asymptotic complexity of both source codes was also mesured, seeking to understand the results obtained during the execution.

## Hardware Methods and Configurations

As the programming language, python 3.7 [3] was used with a computer with the following settings:

- Operating System: Windows 10 Professional, 64-bit
- Processor: Intel Core i5-4200U CPU @ 1.60GHz
- RAM memory: 8.00GB
- SSD: 230 GB

The analyzed datasets consist of 15 files containing respectively the number of nodes in the graph and its adjacency matrix. 
The sizes of analyzed graphs consist of `10, 25, 50, 75, 100, 150, 200, 250, 300, 400, 500, 650, 800,
1000 and 1500` knots. All files were executed and further studied.

## Dijkstra Implementation 

Considering that Dijkstra's algorithm calculates the distance from a node to
all other vertices it was necessary to use a loop to calculate the distance between
all nodes of the graph, calculating all possible paths.

``` def operation_djk(graph_size, graph_matrix, print_results):
    g = Graph(graph_size)
    g.graph = graph_matrix

    start_time = time.time()

    for i in range(0, graph_size):
        g.dijkstra(i, print_results)

    elapsed_time = time.time() - start_time

    return round(elapsed_time, 5)
```
    
 As you can see an object of type graph and the number of vertices of the graph in question is assigned. Then it's assigned
the adjacency matrix that contains the connections of the graph. Subsequently it was calculate all possible distances of the graph, 
finally the time of algorithm execution.


```
def dijkstra(self, src, print_results):
    dist = [sys.maxsize] * self.V             
    dist[src] = 0                               
    sptSet = [False] * self.V                  

    for cout in range(self.V):                  

        u = self.minDistance(dist, sptSet)     
        sptSet[u] = True                       

        for v in range(self.V):
            if self.graph[u][v] > 0 and sptSet[v] == False\
                and dist[v] > dist[u] + self.graph[u][v]:
                dist[v] = dist[u] + self.graph[u][v]
```


The dijkstra()[2] function it is assigned in all the elements of a list the largest representable integer, 
then is stored the value 0 for the distance from the searched node, since the path from a node to it same is 0.
Subsequently another list was created, where all its elements were assigned **False**,  since it's later used to identify 
if the vertex in question has already been visited.

The loop for execute n times (n represents the number of vertices of the analyzed graph), in the next line the minimum 
distance is calculated using the function minDistance() that returns the vertex with the smallest distance from the analyzed 
vertex, then the returned vertex is set as visited in the **sptSet** list.

Finally, a loop for is used to analyze if there is an edge, if the vertex has already been visited and if
the distance from the current vertex is greater than the distance of the returned vertex, plus the initial distance present in the array.


## Floyd-Warshall Implementation

```
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
 ```
 
 As you can see above the definition of a non-existent edge is changed, no longer being
represented as zero, and starting to be identified through the INF notation. Finally
the floyd_warshall function is called, and the size parameters of the
graph in vertices and the adjacency matrix representing the same.

```
def floyd_warshall(graph_size, dist):

    for k in range(graph_size): 
        for i in range(graph_size): 
            for j in range(graph_size): 
                if i == j:     
                    dist[i][j] = 0  
                else:
                    dist[i][j] = min(dist[i][j], (dist[i][k] + dist[k][j]))
```

Here a loop is used to traverses all the vertices present in the graph, another loop is also traversing all the vertices of the graph
representing the beginning of the path, finally the last loop is used traversing all the vertices of the graph representing the destinations. 

Inside this loop it is checked if the beginning and end of the paths are equal, in this case the value assigned to the path is zero, otherwise it is
analyzed if the found path is smaller than the current path, if yes, it is updated the path. 

Through this implementation, the algorithm searches by brute force all the possible paths within the analyzed graph.


## Results and discussion

After executing all the files, an analysis was made through a graph representing
the chronological performance of the two approaches.

Analysis of the density of graphs:

```
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
 ```
 
 In order to allow a deeper analysis of the analyzed dataset, for the entire
analyzed graph, a function named graph_densitiy() was executed, which when receiving the
adjacency matrix that represents the graph, applies the following mathematical formula[4]:

> P = E / (N * (N-1))


Where:  E = Number of Edges
        N = Number of Vertices

Finally, in function a, it is analyzed whether the value of P is less than 1, if so, the graph is
considered sparse, otherwise it is considered dense.


#### Chronological time spent executing the algorithms:

The calculation of the chronological times of each function was done individually
calculating only the time each function executed, leaving aside parts
unnecessary for the calculation such as reading the files. after the
calculation, a joint and separate analysis of the times of each function was performed.
Its graphs and table can be viewed below.

|Files     |Dijkstra's Time (s)  |Floyd Wershall's Time (s)|
| :---:    | :-:         | :-: |
|File 10   |0,001        |0,001                |   
|File 25   |0,01299      |0,02299 |
|File 50   |0,13292      |0,26394 |
|File 75   |2            |1 |
|File 100  |2            | 2 |
|File 150  |5            | 7 
|File 200  |7            |10 |
|File 250  |12           |19 |
|File 300  |12           |14 |
|File 400  |21           |33 |
|File 500  |40           |66 |
|File 650  |87           |141|
|File 800  |163 |263 |
|File 1000 |320 |515 |
|File 1500 |1.079 |1.753| 

As can be inferred by viewing the table, the floyd-warshall runtime was bigger than the Dijkstra runtime. 

For smaller data sets the difference was not significant, but as
the analyzed datasets were getting bigger, the chronological difference ended up becoming bigger. 

One of the possible explanations for the results obtained is that the implementation of the floyd Warshall algorithm considers all paths
possible, so the algorithm analyzes non-existent edges consuming more processing during the process, unlike the dijkstra algorithm that analyzes
only existing edges. To corroborate the performance analysis, within the analyzed set, all graphs are considered spaces according to the formula
implemented.

#### Asymptotic complexity analysis

<p align="center">
  <img src="https://user-images.githubusercontent.com/17886190/159343719-ecbdce85-4a17-40ed-bdb0-462b6732a01f.png"/>
</p>

In the figure above, we arrive at the following complexity of the algorithm:

> O( N<sup>2</sup> ) 

however as the job requirement required the calculation of all paths
possible, the calculated function was executed for the n vertices present in the graph, making thus its final complexity 

> O((N<sup>2</sup>)*n), ie O(N<sup>3</sup>)

<p align="center">
  <img src="https://user-images.githubusercontent.com/17886190/159343800-e8471505-a3bc-4ae5-a567-a9334f7eddf7.png"/>
</p>

Above after analyzing line by line, we arrive at the following complexity of the algorithm:
O(N<sup>3</sup>).

## Conclusion

After the implementation and analysis of the results, it was concluded first, through verification by calculus, that all graphs were sparse, that is, their number of edges was considerably less than the number of vertices. 

Since this check it is possible to observe that given a sparse graph, the running time for Dijkstra will be
shorter than the execution time for Floyd Warshall due to the fact that Dijkstra only checks the distances between vertices where there are edges connecting them, while Floyd Warshall tests all vertices even if there is no edge between them. 

About asymptotic analysis, according to the implementation made, both algorithms had a
complexity of O( N<sup>3</sup> ), a result that corroborates the data found in the literature.


Thus, we conclude that the algorithm used to solve the problem depends on the
dataset, that is, for sparse graphs (few edges between vertices) the solution
the most suitable would be the implementation of dijkstra, as for denser graphs (many edges
between vertices) Floyd Warshall may be the most suitable solution.

## References

[1] [Floyd Warshall](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/?fbclid=IwAR127qd65STnsgV)

[2] [Dijkstra](https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/fbclid=IwAR0Gr5ll5LQxhIRvzAfKIidAWzprvdEGKMBFBXImoDLW9FzZaIfqdG7Fg9g)

[3] [Python](https://www.python.org/)

[4] [Density] - Diestel Reinhard (2005) Graph Theory
