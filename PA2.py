import sys
import argparse
from collections import defaultdict
import heapq

def read_graph(file_path):
    graph = defaultdict(list)
    all_vertices = set() 

    with open(file_path, 'r') as f:
        for line in f:
            parts = line.split(':')
            src = int(parts[0])
            edges = parts[1].split()

            all_vertices.add(src)  

            for i in range(0, len(edges), 2):
                dest = int(edges[i])
                weight = int(edges[i + 1])
                graph[src].append((dest, weight))

                all_vertices.add(dest)  

    for vertex in all_vertices:
        if vertex not in graph:
            graph[vertex] = []  

    return graph

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex]:
            distance = distances[current_vertex] + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distances[neighbor], neighbor))
    
    return distances

def find_shortest_cycle(graph):
    shortest_cycle = float('inf')
    
    for vertex in graph:
        distances = dijkstra(graph, vertex)
        for v in graph:
            # if v != vertex and distances[vertex] != float('inf'):
            if distances[vertex] != float('inf'):
                for dest, w in graph[v]:
                    if vertex == dest:
                        cycle = distances[v] + w
                        if cycle < shortest_cycle:
                            shortest_cycle = cycle
                    
    return shortest_cycle

def main(file_path):
    graph = read_graph(file_path)
    shortest_cycle_length = find_shortest_cycle(graph)
    
    if shortest_cycle_length == float('inf'):
        print("The length of the shortest cycle is: 0")
    else:
        print(f"The length of the shortest cycle is: {shortest_cycle_length}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find the shortest cycle in a directed graph.")
    parser.add_argument('-input', required=True, help="Input graph file")
    args = parser.parse_args()
    
    main(args.input)
